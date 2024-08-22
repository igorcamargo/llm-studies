from modules.llm.ollama_predict import execute as llm_predict

def execute(prompt: str):
    return llm_predict(prompt=prompt)
