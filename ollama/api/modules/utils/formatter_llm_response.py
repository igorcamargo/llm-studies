import re

def formatter_by_sentences(response: str):
    response = response.replace('"', '')
    response = response.replace('\n', '')
    sentences = re.split(r'(?<=[.!?]) +', response.replace('\n', ''))
    
    return [sentence.strip() for sentence in sentences]
