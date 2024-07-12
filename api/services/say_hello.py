def execute(params: dict) -> dict:


    # ========================================
    # Handle data module
    ## Get coach request parameters
    ## Make query DB data
    ## Responses formalized data
    
    # be crative


    # ========================================
    # Prompt builder module
    ## Get formalized data and coach params
    ## Make prompt according template
    ## Responses prompt

    # make prompt
    STATE = 'say_hello'
    prompt_template = f"{STATE}.{agent}"

    ## prompt -> 'say_hello.people'
    llama_prompt = "Você é uma pessoa!"
    llama_prompt = llama_prompt + "Diga oi para seu amigo."




    # ========================================
    # Handle LLM module
    ## Get coach start training prompt
    ## Reques to LLM
    ## GPT | Llama
    ## Get LLM response

    import re
    from ollama import Client

    client = Client(host='http://ollama:11434')
    response = client.generate(
        model='llama3',
        prompt=llama_prompt
    )

    sentences = re.split(r'(?<=[.!?]) +', response['response'].replace('\n', ''))
    sentences = [sentence.strip() for sentence in sentences]


    # Response coach message

    return {
        'prompt': llama_prompt,
        'response': sentences
    }