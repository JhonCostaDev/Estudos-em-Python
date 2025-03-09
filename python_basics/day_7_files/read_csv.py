#%%
import json
file_name = 'data.csv'

with open(file_name) as file:
    content = file.readlines()

#%%
for i, linha in enumerate(content):
    content[i] = linha.strip('\n').split(',')
# %%
def create_list_of_dictionaries(list) -> list:
    """This function takes a list and turns it into a list of dictionaries."""
    head = list[0]
    content = list[1:]
    list_of_dict = []
    id = 1
    for line in content:
        dictionary = dict(zip(head, line))
        dictionary['id'] = id
        list_of_dict.append(dictionary)
        id += 1
    return list_of_dict

def list_to_json(list):
    pass
# %%
dictionaries = create_dict(content)
# %%
with open('data_json.json', 'w') as f:
    json.dump(dictionaries, f, indent=4)
# %%
