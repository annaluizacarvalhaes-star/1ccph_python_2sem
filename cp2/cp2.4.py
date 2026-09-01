def registrar_acesso(dados):
    dados["acessos"] += 1
    return dados

sistema = {
    "acessos": 10
}

resultado = registrar_acesso(sistema)

resultado ["acessos"] += 5

print(sistema["acessos"])