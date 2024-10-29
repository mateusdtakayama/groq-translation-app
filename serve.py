"""
Este módulo define uma API em FastAPI que usa LangChain para fornecer traduções formais e
informais de texto em diferentes idiomas.

Classes e Funções Principais:
- `ChatGroq`: Interface do LangChain para o modelo "gemma2-9b-it", usando a API da Groq para
  processamento de linguagem.
- `ChatPromptTemplate`: Template para criação de prompts de tradução, com mensagens sistemáticas
  para especificar o formato e o estilo das traduções.
- `StrOutputParser`: Parser para extrair a string de saída do modelo, simplificando o
  processamento da resposta.
- `add_routes`: Função do LangServe que adiciona a rota FastAPI, permitindo acesso à cadeia
  (chain) de processamento.

Fluxo de Execução:
1. `ChatPromptTemplate`: Define o prompt de tradução, especificando uma estrutura que instrui o
   modelo a fornecer duas versões de tradução: formal e informal.
2. `ChatGroq`: Executa o prompt usando o modelo "gemma2-9b-it".
3. `StrOutputParser`: Processa a saída do modelo, retornando apenas a tradução.

Variáveis de Ambiente:
- `GROQ_API_KEY`: Chave API da Groq, carregada do arquivo `.env` para autenticação.

Execução:
Inicia o servidor FastAPI com uma rota na URL `/chain`, que recebe texto e idioma como parâmetros
e retorna as traduções.
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
            Traduza o texto: {text} para a linguagem: {language}. Faça duas versões da tradução.
            Escreva apenas a tradução e nada mais, siga esse padrão:
            1. **formal**
            2. **informal**
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
