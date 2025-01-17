import os
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
from io import StringIO

load_dotenv()
api_token = os.getenv("OPENAI_API_KEY")

texto = """
Mais comentadas
    Plano de saúde(26 comentários)
    "Unimed só paga se usar "
    Vale-transporte/Fretado(14 comentários)
    "Bom dependendo da sua localização "
    Plano odontológico(12 comentários)
    "Bom beneficio se usar ele"
    8 de jan. de 2025
Ex-Mecânico Montador em Campo Largo, PR, Paraná
Ótima para trabalhar se preocupa com os funcionários
18 de dez. de 2024
Ex-Funcionário em Piracicaba, SP, São Paulo
Tem muitos benefícios, plano odontológico
5 de dez. de 2024
Funcionário — Piracicaba, SP, São Paulo (cargo atual)
Ótima empresa para se trabalhar
"""

client = OpenAI(api_key=api_token)

messages = [
    {"role": "system", "content": texto},
    {"role": "user", "content": "Analyze these comments and classify them into positive, negative, or neutral, and create a table with city and classification. Quero apenas a tabela."}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0
)

# Extract the table content from the response
table_content = response.choices[0].message.content

# Read the table into a DataFrame
df = pd.read_table(StringIO(table_content), sep=' *\| *', engine='python')

# Print the DataFrame 
print(df)

# Save the DataFrame to a CSV file
df.to_csv('sentiment_analysis.csv', index=False)