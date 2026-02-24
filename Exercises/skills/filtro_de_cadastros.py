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
