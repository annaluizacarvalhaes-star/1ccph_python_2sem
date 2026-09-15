# Aula 4 - Buscar um usuário e exportar os dados

from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    company = input("Company: ")
    stage = input("Estafio de vendas: ")

    if not name or not email or "@" not in email:
        print("Nome e\ou email válido são obrigatórios")
        return # volta para o Menu inicial

    print( name, email, company, stage )

    # precisar de model para modelar os dados
    print(model_lead(name, email, company, stage))

    # depois de modelado...
    # chamar control.py para enviar os dados modelados para o banco de dados json
    control.created_lead(model_lead(name,company, email, stage))

def list_lead():
    leads = control.read_leads()

    if not leads:
        print("nenhum lead ainda")
        return

    print("\n# | NOME           | COMPANY                   | EMAIL ")
    for i, lead in enumerate(leads):
        print(f"{i: 02d} | {lead['name']: <20} | {lead['company']: <17} | {lead['email']: <20}")

def search_leads():
    query = input("Buscar por: ").strip().lower() # Tira os espaços e deixa tudo minúsculo
    if not query:
        print("Consulta vazia")
        return []

    # Nesse momento irei enviar minha busca para control
    # o control.read_leads_search() irá retornar com um array com os leads encontrados
    leads_finded = control.read_leads_search(query)

    print("\n# | NOME           | COMPANY                   | EMAIL ")
    for i, lead in enumerate(leads_finded):
        print(f"{i: 02d} | {lead['name']: <20} | {lead['company']: <17} | {lead['email']: <20}")
 # i = ao incice do array na lista em json


def export_leads(): # criar um arquivo sv na pasta data
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não é possivel exportar os leads para csv")
    else:
        print(f"CSV exportado para {path_csv}")


def  main():
    while True:
        print("\nMini CRM - 1° aula - (adicionar / listar usuarios")
        print("[1] - adicionar lead")
        print("[2] - listar lead")
        print("[3] - Buscar (nome/ email/ empresa)")
        print("[4] - Exportar como CSV")
        print("[0] -sair do programa")

        opt = input("Escolha uma ação: ").strip() # tirar o espaço
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_lead()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Saindo do programa")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()