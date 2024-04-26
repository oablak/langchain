
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

print(os.getenv("OPENAI_API_KEY"))

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
response = llm.invoke("What is the capital of Russia ?")

print(response.content)

