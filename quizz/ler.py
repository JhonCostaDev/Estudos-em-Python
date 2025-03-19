import json
json_path ='json/kcs.json'

def read_json(json_file) -> list:
    with open(json_file, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        
    return data

arquivo = read_json(json_path)

#print(arquivo)

def load_question(index=0):
    data = read_json()
    
    