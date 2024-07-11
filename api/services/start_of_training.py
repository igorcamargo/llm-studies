def execute(params: dict) -> dict:


    # ========================================
    # Handle data module
    ## Get coach request parameters
    ## Make query DB data
    ## Responses formalized data
    
    # get agent type
    agent = params.get('agent')
    
    if agent not in ['coach']:
        raise Exception('Agent not found!', 404)
    
    # get agent params
    agent_params = params.get('params')

    if not agent_params:
        raise Exception('Params is required!', 400)
    
    # get required agent params
    required_agent_params = ['tpn', 'un']

    if not all(key in agent_params for key in required_agent_params):
        raise Exception('Invalid agent parameters!', 400)



    
    # ========================================
    # Prompt builder module
    ## Get formalized data and coach params
    ## Make prompt according template
    ## Responses prompt

    # make prompt
    STATE = 'start_of_training'
    prompt_template = f"{STATE}.{agent}"

    ## prompt -> 'start_of_training.coach'
    llama_prompt = "You are Goalkeeper Coach. "
    llama_prompt = llama_prompt + f"Beginning of the {agent_params.get('tpn')} training plan. "
    llama_prompt = llama_prompt + "Greet the athlete and ask them to adjust both the position and size of the goal to your preferences. "
    llama_prompt = llama_prompt + f"\"Hello, {agent_params.get('un')}! Welcome to today's {agent_params.get('tpn')}. I'm excited to start our session and help you improve your goalkeeping skills. To begin, could you please adjust both the position and size of the goal to your preferences? Let's make sure everything is set up just right so we can have an effective training today. Looking forward to a great session together!\". "
    llama_prompt = llama_prompt + "Additional Instructions: Generate variations of this message that are friendly, motivating and personalized, shorts, and ensuring the athlete feels welcomed and ready to train. "
    llama_prompt = llama_prompt + "Always add the athlete's name and the name of the day's training in the answer."




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
        # 'coach': 'hello!',
        # 'prompt': llama_prompt,
        'response': sentences
    }