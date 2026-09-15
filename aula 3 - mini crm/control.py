# repo.py

from pathlib import Path # caminho de arquivos
import json, csv

DATA_DIR = Path(__file__).resolve().parent/'data'
print(DATA_DIR)

DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR/'leads.json'

# CRUD
# CREATE - create_lead()
# READ - read_lead()
# UPDATE
# DELETE

def read_leads():
    if not DB_PATH.exists(): # Path do banco de dados - Diretório do banco de dados (caminho)
        return[]

    try:  # loads carrega o Path e manda ao banco de dados
        return json.loads(DB_PATH.read_text(encoding = "UTF-8")) # Leio o leads.jason
    except json.JSONDecodeError:
        # se corromper, retorna vazio
        return[]

def created_lead(lead_dict): # recebe como parametro o diccionário do lead
    leads = read_leads() # lista de leads
    leads.append(lead_dict) # Adiciono o dicionário ao final dessa lista

    DB_PATH.write_text(json.dumps(leads, ensure_ascii= False, indent=2), encoding="utf-8")
    # Converte para Jason,  ident=2 (melhor visualização), enconding="uft-8" - caracters especiais

def read_leads_search(query):
    leads = read_leads() # lista de leads
    results = []


    for i, lead in enumerate(leads):
  # Posição 0 será o primeiro dicionário da lista completo, e não a primeira variável
        txt_lead = f"{lead["name"]} {lead["name"]} {lead["company"]} {lead["email"]}".lower()

        if query in txt_lead:
            results.append(lead)

    if not results:
        print("Nada encontrado")
        return []
    else:
        return results

def export_csv():
    # Exporta o lead para CSV e retorna o path de onde o arquivo foi salvo
    path_csv = DATA_DIR/'leads.csv'
    leads = read_leads()

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file: # file - arquivo
            writer = csv.DictWriter(file, fieldnames = leads[0].keys())
            writer.writeheader()
            for row in leads:
                writer.writerow(row) # peço para escrever uma linha, a linha = row
        return path_csv

    except PermissionError:
     return None


