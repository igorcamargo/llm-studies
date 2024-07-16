import re
from gpt4all import GPT4All

def execute(prompt: str, behaviour: str):
    model = GPT4All(model_name='orca-mini-3b-gguf2-q4_0.gguf')
    system_prompt = f"### System:\n{behaviour}\n\n"
    
    with model.chat_session(system_prompt=system_prompt):
        response = model.generate(prompt=prompt, top_k=1)

    return response.replace('"','').strip()