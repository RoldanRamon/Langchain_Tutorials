from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Busca a chave da API no arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_token)

messages = [{"role": "system", "content": "You are a helpful math tutor."}]
print("Digite 'sair' para encerrar o chatbot.")

while True:
    # Recebe a mensagem do usuário
    user_msg = input("User: ")
    
    # Verifica se o usuário quer encerrar o chatbot
    if user_msg.lower() == "sair":
        print("Chatbot encerrado.")
        break
    
    # Adiciona a mensagem do usuário ao histórico
    user_dict = {"role": "user", "content": user_msg}
    messages.append(user_dict)
    
    # Cria a solicitação para a API da OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=100
    )
    
    # Adiciona a resposta do assistente ao histórico e exibe a resposta
    assistant_msg = response.choices[0].message.content
    assistant_dict = {"role": "assistant", "content": assistant_msg}
    messages.append(assistant_dict)
    
    print("Assistant:", assistant_msg, "\n")
