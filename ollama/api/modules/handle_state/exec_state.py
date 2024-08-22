import importlib
from modules.handle_params.validate import required_agent_param
from modules.llm.predict import execute as exec_predict
from modules.utils.formatter_llm_response import formatter_by_sentences

def execute(state: str, params: dict, agents: dict, required_agent_params: dict) -> dict:
    required_agent_param(params=params, agents=agents, required_agent_params=required_agent_params)
    
    module = importlib.import_module(f"modules.prompt_templates.{state}_{params.get('agent')}")
    get_prompt = getattr(module, 'get_prompt') 
    predict = exec_predict(prompt=get_prompt(params.get('params')))

    return __process_response(predict)


def __process_response(predict):
    if isinstance(predict, dict):
        return {'response': formatter_by_sentences(predict['response'])}
    return {'response': formatter_by_sentences(predict)}
