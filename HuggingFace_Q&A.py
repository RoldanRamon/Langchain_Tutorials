from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Busca a chave da API Hugging Face do arquivo .env
api_token = os.getenv("HUGGINGFACE_API_KEY")

llm = HuggingFaceEndpoint(
    repo_id='HuggingFaceH4/zephyr-7b-beta',
    # repo_id='tiiuae/falcon-7b-instruct',
    huggingfacehub_api_token=api_token
)

question = 'Meu sobrenome é Roldan. Me conte curiosidades sobre a origem do meu sobrenome. Responda em Portugues.'
output = llm.invoke(question)
print(output)