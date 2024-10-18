from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Busca a chave da API do arquivo .env
api_token = os.getenv("OPENAI_API_KEY")


learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a plan to help me hit this goal: {learning_plan}."
)

llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_token)

# Complete the sequential chain with LCEL
seq_chain = ({"activity": learning_prompt | llm | StrOutputParser()}
    | learning_prompt
    | llm
    | StrOutputParser())

# Call the chain
print(seq_chain.invoke({"activity": "comer carne"}))