# initialize simple vector indices + global vector index
import os
import openai
from llama_index import ServiceContext, StorageContext, VectorStoreIndex, SimpleDirectoryReader, load_index_from_storage

with open("apikey", "r") as f:
    openai.api_key = f.read().strip()

if __name__ == "__main__":
    # initialize simple vector indices + global vector index
    service_context = ServiceContext.from_defaults(chunk_size=512)
    index_set = {}
    for chapter in os.listdir("chapters"):
        docs = SimpleDirectoryReader("chapters/" + chapter).load_data()
        storage_context = StorageContext.from_defaults()
        cur_index = VectorStoreIndex.from_documents(
            docs,
            service_context=service_context,
            storage_context=storage_context,
        )
        index_set[chapter] = cur_index
        storage_context.persist(persist_dir=f'./storage/{chapter}')
        print("Loaded", chapter)


def load_indices():
    # load indices from disk
    index_set = {}
    for chapter in os.listdir("chapters"):
        storage_context = StorageContext.from_defaults(persist_dir=f'./storage/{chapter}')
        cur_index = load_index_from_storage(storage_context=storage_context)
        index_set[chapter] = cur_index
    return index_set
