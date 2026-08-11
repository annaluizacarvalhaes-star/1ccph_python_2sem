
endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]
print(endpoints[0])
print(status[0][2])

def eh_sucesso(codigo):
    return 200 <= codigo <= 299
# print(eh_sucesso(status[2][1]))


#Função que valida na lista de req de UM endpoint SE tem DOIS erros seguidos
# status [0] = [200, 200, 401, 200, 500] ---- false
# status[2] = [201, 500, 502, 201, 500] --- True
# essa ultima lista é respostas_http

def erros_seguidos(resposta_http):
    for i in range(len(resposta_http) - 1):
        codigo_atual = resposta_http[i]
        prox_codigo = resposta_http[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False  # fora do for

# [201, 500, 502, 201, 500]  -- respostas_http
def analisar_edpiont(resposta_http):
    qtd_sucessos = 0

    for cod_http in resposta_http:
        if eh_sucesso(cod_http):
            qtd_sucessos += 1

    qtd_total_req = len(resposta_http)
    qtd_erros = qtd_total_req - qtd_sucessos

    percentual_sucessos = (qtd_sucessos / qtd_total_req) * 100

    tem_erros_seguidos = erros_seguidos(resposta_http)

    if tem_erros_seguidos:
        classificacao = "CRITICO"
    elif tem_erros_seguidos:
        classificacao = "ESTAVEL"
    else:
        classificacao = ("INSTAVEL")

    return (qtd_sucessos, qtd_erros, percentual_sucessos, classificacao)

# PERCORRER TODA A MATRIZ
maior_qtd_erros = -1
endpoint_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    respostas_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_edpiont(respostas_endpoint)

    print (f"Endpoint: {nome_endpoint}")
    print(f"Repostas http: {respostas_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"Percentual: {percentual}")
    print(f"Classificacao: {classificacao}")
    print("---" * 20)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erro = nome_endpoint

print(f"Endpoint com mais erros: {endpoint_maior_erro}")



