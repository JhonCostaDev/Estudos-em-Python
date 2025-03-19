#%%
import requests
import json
from tqdm import tqdm
#%%

def get_data(url)->list:
    
    response = requests.get(url)
    if response.status_code == 200:
        response= response.json()
        dictionary = response

    return dictionary

def save_json(file_path, dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dict, file,ensure_ascii=False, indent=4)
#%%
url = 'https://dummyjson.com/users'
file_path = 'data_json.json'
# %%
data = get_data(url=url)

#%%
save_json(file_path=file_path, dict=data)
# %%
