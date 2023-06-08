from dotenv import load_dotenv
from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os

#load environment vars
load_dotenv()

#generate llama directory reader to index it
documents = SimpleDirectoryReader(os.getenv("TELEGRAM_BOT_API_KEY")).load_data()
#generate the index with the directory reader
index = VectorStoreIndex.from_documents(documents)

#store the index in storage/ folder 
index.storage_context.persist()
