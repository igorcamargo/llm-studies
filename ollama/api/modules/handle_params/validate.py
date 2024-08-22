def required_agent_param(params: dict, agents: dict, required_agent_params: dict):
    agent = params.get('agent')
    if not agent:
        raise Exception('Agent is required!', 400)
    if agent not in agents:
        raise Exception('Agent not found!', 404)
    
    if params.get('params'):
        if not all(key in params.get('params') for key in required_agent_params):
            raise Exception('Invalid agent parameters!', 400)
