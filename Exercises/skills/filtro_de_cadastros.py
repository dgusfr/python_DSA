"""
Você está construindo o endpoint de cadastro de usuários. O Front-end envia um lote de usuários de uma vez. Você precisa separar quem pode ser salvo no banco de dados e quem deve ser rejeitado.

**Regras de Negócio para um usuário ser "Válido":**

1. **Nome:** A chave `"nome"` deve existir e ter pelo menos 2 caracteres.
2. **Idade:** A chave `"idade"` deve existir, ser um número, e ser maior ou igual a 18.
3. **Email:** A chave `"email"` deve existir e obrigatoriamente conter o caractere `"@"`.

Se falhar em **qualquer** uma dessas regras, o usuário é considerado "Inválido".

**Dados de Entrada:**

```python
cadastros = [
    {"id": 1, "nome": "Ana", "idade": 25, "email": "ana@email.com"}, # Válido
    {"id": 2, "nome": "B", "idade": 30, "email": "bob@email.com"},   # Inválido (nome curto)
    {"id": 3, "nome": "Carlos", "idade": 17, "email": "carlos@email.com"}, # Inválido (menor de 18)
    {"id": 4, "nome": "Diana", "email": "diana@email.com"},          # Inválido (sem idade)
    {"id": 5, "nome": "Eva", "idade": 28, "email": "eva.email.com"}, # Inválido (sem @ no email)
    {"id": 6, "nome": "Fabio", "idade": 40, "email": "fabio@email.com"} # Válido
]

```

**Resultado Esperado:**
Sua função deve retornar um **dicionário** separando os IDs válidos dos inválidos.

{
    "validos": [1, 6],
    "invalidos": [2, 3, 4, 5]
}

"""

cadastros = [
    {"id": 1, "nome": "Ana", "idade": 25, "email": "ana@email.com"},
    {"id": 2, "nome": "B", "idade": 30, "email": "bob@email.com"},
    {"id": 3, "nome": "Carlos", "idade": 17, "email": "carlos@email.com"},
    {"id": 4, "nome": "Diana", "email": "diana@email.com"},
    {"id": 5, "nome": "Eva", "idade": 28, "email": "eva.email.com"},
    {"id": 6, "nome": "Fabio", "idade": 40, "email": "fabio@email.com"},
]


def filtrar_cadastros(cadastros):
    resultado = {"validos": [], "invalidos": []}

    for cadastro in cadastros:
        id_usuario = cadastro.get("id")
        nome = cadastro.get("nome", "")
        idade = cadastro.get("idade")
        email = cadastro.get("email", "")

        if (
            isinstance(nome, str)
            and len(nome) >= 2
            and isinstance(idade, (int, float))
            and idade >= 18
            and isinstance(email, str)
            and "@" in email
        ):
            resultado["validos"].append(id_usuario)
        else:
            resultado["invalidos"].append(id_usuario)
    return resultado


print(filtrar_cadastros(cadastros))
