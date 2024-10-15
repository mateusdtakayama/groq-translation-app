"""
The `os` module provides a way to interact with the operating system. 
It includes functions for file and directory manipulation, environment 
variables access, and path operations. Common functionalities include:

- Accessing and modifying the file system (e.g., creating, deleting files).
- Retrieving environment variables (e.g., `os.getenv()`).
- Working with paths and directories (e.g., `os.path`).
- Managing processes and system-specific parameters.

This module is essential for applications that require OS-level interactions.
"""

import os
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)


PROMPT_TEMPLATE = """
Translate the following text: {text} into {language} in this pattern:
Original text: {text}
Translated text: **translation**
"""
prompt = ChatPromptTemplate.from_messages(
    [("system", PROMPT_TEMPLATE), ("user", "{text}")])

parser = StrOutputParser()

chain = prompt | model | parser

app = FastAPI(title="Langchain Server", version="0.1.0",
              description="A simple API server using Langchain runnable interfaces")

add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
