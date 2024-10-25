from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Busca a chave da API do arquivo .env
api_token = os.getenv("NEMOTRON_API_KEY")

llm = ChatNVIDIA(model="mistralai/mixtral-8x7b-instruct-v0.1",
                 max_tokens=1024,
                 api_key=api_token)

question = 'Meu sobrenome é Roldan. Me conte curiosidades sobre a origem do meu sobrenome. Responda em Portugues.'
output = llm.invoke(question)
print(output)
