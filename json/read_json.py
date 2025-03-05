import json


file_path = 'json/review_cap1.json'

def load_and_convert_json_to_dict(json_file) -> dict:
    """Carrega um arquivo JSON, transforma em um dicionario python."""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def load_question(dictionary, list_position=0) -> dict:
    key = list(dictionary.keys())[0]
    list_lenght = len(dictionary[key]) # tamanho 
    list_questions = dictionary[key]

    return list_questions[list_position]

def show_question(dictionary):
    question_number = dictionary['questionNumber']
    question = dictionary['questionText']
    dict_options = dictionary['options']
    
    print(dictionary['questionText'])
    for tag, option in dict_options.items():
        print(f'({tag}): {option}')
    


def get_user_choise():
    user_choise = input('Type your answer\n')
    #validate answer



# function to verify the answer


#print(type(load_and_convert_json_to_dict(file_path)))
#print(load_question(load_and_convert_json_to_dict(file_path)))
show_question(load_question(load_and_convert_json_to_dict(file_path)))
get_user_choise()














# dados = {
#     'dog':[
#         {
#         "name": "fulio",
#         "color": "black"
#         },
#         {
#         "name": "menina",
#         "color": "black"
#         },
#         {
#         "name": "jr",
#         "color": "black"
#         },
#     ]
# }
# print(dados.keys())
# print(dados.items())