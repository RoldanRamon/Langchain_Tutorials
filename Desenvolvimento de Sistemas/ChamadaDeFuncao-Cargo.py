from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# Busca a chave da API no arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

# Define the message listing
message_listing = [{'role': 'user',
  'content': """We are currently seeking a highly skilled
Data Scientist to join our innovative team at
the company's headquarters in San Francisco,
CA. In this role, you will have the opportunity
to work on complex data analysis and
modeling projects that drive our strategic
decisions. Requirements: Minimum 3 years of
experience in data science with Python and
AWS, Azure or GCP."""}]

# Add the function definition
function_definition = [{
  'type': 'function',
  'function': {
    'name': 'extract_job_info',
    'description': 'Get the job information from the body of the input text',
    'parameters': {
      'type': 'object',
      'properties': {
        'job': {
          'type': 'string',
          'description': 'Job title'
        },
        'location': {
          'type': 'string',
          'description': 'Office location'
        },
        # Add other properties as needed
      }
    }
  }
}]

# Create the OpenAI client
client = OpenAI(api_key=api_token)

# Call the API
response= client.chat.completions.create(
    model="gpt-4o-mini",
    # Add the message
    messages = message_listing,
    # Add your function definition
    tools = function_definition
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)