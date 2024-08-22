from modules.handle_state.exec_state import execute as exec_state

def execute(state: str, params: dict) -> dict:
    agents                  = ['people']
    required_agent_params   = []

    return exec_state(state, params, agents, required_agent_params)
