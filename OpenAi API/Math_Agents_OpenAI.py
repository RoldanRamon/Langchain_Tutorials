from langchain_openai import ChatOpenAI
# from langchain.agents import load_tools
from langchain_community.agent_toolkits.load_tools import load_tools
from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Busca a chave da API do arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

# Cria a chamada da llm
llm = ChatOpenAI(model="gpt-4o-mini", api_key= api_token, temperature=0)

# Instancia qual ferramenta será utilizada
tools = load_tools(["llm-math"],llm=llm)
# tools = load_tools(["wikipedia"])

# Função que o agente usa para responder com a llm e ferramenta
agent  = create_react_agent(llm,tools)

# Invoca função para responder a pergunta
messages = agent.invoke({"messages": [("quanto é dois mais tres?")]})

# Mostra resultado completo
print(messages)

# Mostra Resultado especifico
print(messages['messages'][-1].content)