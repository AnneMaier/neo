import ollama

response = ollama.chat(
    model = 'llama3:latest', 
    messages = [
        {'role' : 'system', 'content' : 'You are a python expert.' },
        {'role' : 'user', 'content' : 'Code a python function to generate a Fibonacci sequence.' }
    ]
)

print(response['message']['content'])