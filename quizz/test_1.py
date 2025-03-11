#%%
import json
#%%
json_path = '/home/jonathan/Documents/myGitHub/Estudos-em-Python/json/kcs.json'

def read_json(json_file) -> list:
    with open(json_file, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        
    return data

def show_question_cli(tuple)->None:
    tags = ['A', 'B', 'C', 'D']
    print(f"{tuple[0]}) {tuple[1]}")
    for index, option in enumerate(tuple[2]):
        print(f'{tags[index]}) {option}')

#TODO: In the function below, I have to abstract the key to accept any variables name...
def load_question(list, item=0) -> dict:
    dictionary = list[item]
    question_number = dictionary.get('question')
    question = dictionary.get('text')
    options = dictionary.get('choices')
    #answer = dictionary.get('answer')
    
    return question_number, question, options
    
# %%

data = read_json(json_file=json_path)
question = load_question(data)
show_question_cli(question)
#print(data[0])

# %%
