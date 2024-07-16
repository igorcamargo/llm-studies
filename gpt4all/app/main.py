import sys

# sys.path.append('/app/modules/gpt4all')
from modules.gpt4all.execute import execute


def make_prompt() -> str:
    return 'Say hello to friend.'


def make_behaviour() -> str:
    return 'You are cool people.'


print("Generate LLM")
response = execute(prompt=make_prompt(), behaviour=make_behaviour())
print(response)