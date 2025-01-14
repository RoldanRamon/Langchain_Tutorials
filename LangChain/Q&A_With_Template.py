from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Busca a chave da API do arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are soto zen master Roshi."),
        ("human", "What is the essence of Zen?"),
        ("ai", "When you are hungry, eat. When you are tired, sleep."),
        ("human", "Respond to the question: {question} in portuguese of Brazil")
    ]
)

llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_token)
llm_chain = prompt_template | llm
question = "Quantidade de titulos mundiais de futebol masculino até 2024 separado por país?"
response = llm_chain.invoke({"question": question})
print(response.content)
