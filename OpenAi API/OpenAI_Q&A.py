from langchain_openai import OpenAI
# from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Busca a chave da API no arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    # model='gpt-4o-mini',
    api_key=api_token
)

question = 'Meu sobrenome é Roldan. Me conte curiosidades sobre a origem do meu sobrenome. Responda em Portugues.'
output = llm.invoke(question)
print(output)