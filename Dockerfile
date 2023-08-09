FROM python:3.9-slim-buster

WORKDIR /nush-llm-chatbot

COPY . .
RUN pip install -r requirements.txt
RUN python llamaindex/vector_indices.py


CMD ["python", "-m", "frontend.app"]