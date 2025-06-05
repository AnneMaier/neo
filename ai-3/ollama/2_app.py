from openai import OpenAI
import os


ollama_host = os.environ["OLLAMA_HOST"]

client = OpenAI(
    base_url = f'{ollama_host}/v1',
    api_key='ollama',
)

response = client.chat.completions.create(
    model = 'llama3:latest',
    messages = [
        {'role': 'system', 'content': 'You are a python expert. '},
        {'role': 'user', 'content': 'Code a Python function to generate a Fibonacci sequence.'}
    ]
)

result = response.choices[0].message.content
print(result)