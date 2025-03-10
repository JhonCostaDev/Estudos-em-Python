#%%
import requests
import json
from tqdm import tqdm
#%%
def get_ceps(list)->dict:
    list_ceps = []
    for cep in tqdm(list):
        api_url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(api_url)
        if response.status_code == 200:
            response= response.json()
            list_ceps.append(response)

    return list_ceps
def save_json(file_path, list):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(list, file,ensure_ascii=False, indent=4)

#%%
ceps = [
    "60160-230",
    "60175-055",
    "60060-120",
    "60810-180",
    "60864-310",
    "60330-190",
    "60710-140",
    "60455-490",
    "60520-132",
    "60833-065",
    '60543315'
]

# %%

data = get_ceps(ceps)
data
# %%
file = 'ceps.json'
save_json(file, data)
# %%
