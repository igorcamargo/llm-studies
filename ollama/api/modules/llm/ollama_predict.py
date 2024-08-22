from ollama import Client

def execute(prompt: str):
    client = Client(host='http://ollama:11434')
    
    return client.generate(
        model='llama3',
        prompt=prompt
    )
