# repo.py

from pathlib import Path # caminho de arquivos
import json

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
    if not DB_PATH.exists():
        return[]

    try:
        return json.loads(DB_PATH.read_text(encoding = "UTF-8"))
    except json.JSONDecodeError:
        # se corromper, começar vazio
        return[]

def created_lead(lead_dict):
    leads = read_leads() # lista de leads
    leads.append(lead_dict)

    DB_PATH.write_text(json.dumps(leads, ensure_ascii= False, indent=2), encoding="utf-8")