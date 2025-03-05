import json


file_path = 'json/review_cap1.json'

def load_and_convert_json_to_dict(json_file) -> dict:
    """Carrega um arquivo JSON, transforma em um dicionario python."""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def load_question(dictionary, list_position=0, chapter=0) -> dict:
    key = list(dictionary.keys())[chapter]
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
    valid_options = ['A', 'B', 'C', 'D']
    while True:
        user_choise = input('Type your answer\n').upper()
        if user_choise in valid_options:
            return user_choise
        print('Invalid option, please choise A, B, C, and D')
    
    
#validate answer

def check_answer(user_answer, selected_question):
    asnwer = user_answer
    question = selected_question['options']
    correct_answer = selected_question['answer']
    # print(question[asnwer])
    # print(corect_answer)
    
    if question[asnwer] == correct_answer:
        return True
    else:
        return False
    



# function to verify the answer


#print(type(load_and_convert_json_to_dict(file_path)))
#print(load_question(load_and_convert_json_to_dict(file_path)))

# show_question(load_question(load_and_convert_json_to_dict(file_path), 1))
#get_user_choise()
def main():
    data = load_and_convert_json_to_dict(file_path)
    question = load_question(data)
    show_question(question)
    answer = get_user_choise()
    print(check_answer(answer, question))
    

main()












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