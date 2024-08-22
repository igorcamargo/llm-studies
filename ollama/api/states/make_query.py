from modules.handle_state.exec_state import execute as exec_state

def execute(state: str, params: dict) -> dict:
    agents                  = ['sql']
    # required_agent_params   = ['filter_field','filter_value','table']
    required_agent_params   = ['command']

    return exec_state(state, params, agents, required_agent_params)
