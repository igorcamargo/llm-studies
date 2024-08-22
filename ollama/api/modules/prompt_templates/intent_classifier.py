def get_prompt(params: dict) -> str:
    prompt = "Você é uma pessoa!"
    prompt += " Diga oi para seu amigo."
    prompt = "tags possíveis: problema_fatura, problema_cartão, pagamento_errado. "
    prompt += "Tag recebida: não_consigo_pagar_fatura_cartão. "
    prompt += "Qual é a Tag possível de acordo com a Tag recebida?"

    return prompt
