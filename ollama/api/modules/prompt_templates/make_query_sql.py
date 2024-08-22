def get_prompt(params: dict) -> str:
    prompt = "Existe a seguinte estrutura da dados em um database mysql: "
    prompt += """CREATE TABLE Clientes (
        cliente_id INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        telefone VARCHAR(15),
        endereco VARCHAR(255),
        data_nascimento DATE
    );"""
    prompt += """, e também essa: CREATE TABLE ContasBancarias (
        conta_id INT PRIMARY KEY AUTO_INCREMENT,
        cliente_id INT,
        banco VARCHAR(100) NOT NULL,
        agencia VARCHAR(10) NOT NULL,
        numero_conta VARCHAR(20) UNIQUE NOT NULL,
        tipo_conta VARCHAR(20) CHECK (tipo_conta IN ('Corrente', 'Poupança')),
        saldo DECIMAL(15, 2) DEFAULT 0.00,
        FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id) ON DELETE CASCADE
    );"""
    prompt += f" Faça o seguinte \"{params.get('command')}\". "
    prompt += "Retorna apenas a query válida, sem explicações."

    return prompt

'''
O método formatter_by_sentences quebra a query. Como poderia ajustar?
```sql
SELECT c.*
FROM Clientes c
JOIN ContasBancarias cb
  ON c.cliente_id = cb.cliente_id
WHERE c.data_nascimento < DATE_SUB(CURDATE(), INTERVAL 20 YEAR)
  AND cb.tipo_conta = 'Poupança'
  AND cb.agencia = 'ABC';
```
'''