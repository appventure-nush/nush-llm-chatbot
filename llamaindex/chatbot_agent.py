import os
import openai
from llama_index import ListIndex, LLMPredictor, ServiceContext, StorageContext
from langchain import OpenAI
from llama_index.indices.composability import ComposableGraph
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from llama_index.langchain_helpers.agents import LlamaToolkit, create_llama_chat_agent, IndexToolConfig
from llama_index.indices.query.query_transform.base import DecomposeQueryTransform
from llama_index.query_engine.transform_query_engine import TransformQueryEngine

from llamaindex import vector_indices

index_set = vector_indices.load_indices()
with open("apikey", "r") as f:
    API_KEY = f.read().strip()
openai.api_key = API_KEY

# describe each index to help traversal of composed graph
index_summaries = [f"Physics notes for {chapter}" for chapter in os.listdir("chapters")]

# define an LLMPredictor set number of output tokens
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, max_tokens=512, openai_api_key=API_KEY))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
storage_context = StorageContext.from_defaults()

# define a list index over the vector indices
# allows us to synthesize information across each index
graph = ComposableGraph.from_indices(
    ListIndex,
    [index_set[chapter] for chapter in os.listdir("chapters")],
    index_summaries=index_summaries,
    service_context=service_context,
    storage_context=storage_context,
)

# define a decompose transform
decompose_transform = DecomposeQueryTransform(
    llm_predictor, verbose=True
)

# define custom retrievers
custom_query_engines = {}
for index in index_set.values():
    query_engine = index.as_query_engine()
    query_engine = TransformQueryEngine(
        query_engine,
        query_transform=decompose_transform,
        transform_metadata={'index_summary': index.index_struct.summary},
    )
    custom_query_engines[index.index_id] = query_engine
custom_query_engines[graph.root_id] = graph.root_index.as_query_engine(
    response_mode='tree_summarize',
    verbose=True,
)

# construct query engine
graph_query_engine = graph.as_query_engine(custom_query_engines=custom_query_engines)

# tool config
graph_config = IndexToolConfig(
    query_engine=graph_query_engine,
    name=f"Graph Index",
    description="useful for when you want to answer queries that require analyzing multiple chapters within the Physics syllabus.",
    tool_kwargs={"return_direct": True}
)

# define toolkit
index_configs = []
for chapter in os.listdir("chapters"):
    query_engine = index_set[chapter].as_query_engine(
        similarity_top_k=3,
    )
    tool_config = IndexToolConfig(
        query_engine=query_engine,
        name=f"Vector Index {chapter}",
        description=f"useful for when you want to answer queries about {chapter}",
        tool_kwargs={"return_direct": True}
    )
    index_configs.append(tool_config)

toolkit = LlamaToolkit(
    index_configs=index_configs + [graph_config],
)

memory = ConversationBufferMemory(memory_key="chat_history")
llm=OpenAI(temperature=0, openai_api_key=API_KEY)
agent_chain = create_llama_chat_agent(
    toolkit,
    llm,
    memory=memory,
    verbose=True
)

if __name__ == "__main__":
    print("Agent initialised!")
    agent_chain.run(input="Compare/contrast the concepts described across the chapters.")
