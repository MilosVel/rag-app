# This file need to be executed in developement if we want to change vector colection for example from dim=3072 to dim =1024

from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")
client.delete_collection("docs")