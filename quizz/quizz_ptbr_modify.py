#%%
import json
import os
import time
#%%
#json_path = '/Estudos-em-Python/json/kcs.json'
json_path ='json/kcs.json'
def first_screen():
    #exibir menu inicial
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
{'#'* 100}
|
|                        SIMULADO Questões KCs AWS ReStart
|
{'#'* 100}
''')
    
    input("Presione Enter para iniciar ...")
    
def read_json(json_file) -> list:
    with open(json_file, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        
    return data

def show_question_cli(tuple, question_number)->None:
    tags = ['A', 'B', 'C', 'D']
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{question_number}) {tuple[1]}\n\n")
    for index, option in enumerate(tuple[2]):
        print(f'{tags[index]}) {option}\n')

#TODO: In the function below, I have to abstract the key to accept any variables name...
def load_question(list, item=0) -> tuple:
    dictionary = list[item]
    question_number = dictionary.get('question')
    question = dictionary.get('text')
    options = dictionary.get('choices')
    answer = dictionary.get('answer')
    answer_type = type(answer).__name__ # aqui n'ao [e] do options, sim so answer
    answer_len = len(answer) # so pegar quando o type for list
    return question_number, question, answer_len, answer_type, options, answer #
    
# Get user answer
#TODO: receber mais que 4 opcoes de multipla escolha
def get_user_choise():
    """Take the user option"""
    #usar o asnwer len para controlar o numero de respostas dada pelo usuario
    
    valid_options = ['A', 'B', 'C', 'D']
    while True:
        user_choise = input('Digite sua resposta\n').upper()
        if user_choise in valid_options:
            return user_choise
        print('Opção inválida, por favor escolha: A, B, C, ou D')

# TODO: Modificar função abaixo para acitar multipla resposta
# TODO: receber tres opcoes de respostas 
def verify_answer(tuple, user_answer, item=0):
    tags_options = ['A', 'B', 'C', 'D']
    answer_type = tuple[-3] #aqui o tipo
    options = tuple[-2]
    answer = tuple[-1]
    correct_index = 0
    

    if options_type == 'str':
        for index, item in enumerate(tags_options):
            if user_answer == item:
                correct_index = index
                
        if answer == options[correct_index]:
            return True
        else:
            return False
    else:
        pass
        # como o usuario digitara multipla respota


def show_score(score, list_data):
    total_question = len(list_data)
    
    if score == 0:
        return 0
    
    result = (score / total_question) * 100
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=' * 100)
    print(f'Você acertou {score} das {total_question} questões')
    print(f"\nA porcentagem de acertos é: {result:.2f}%")
    print('=' * 100)
# %%
def main():
    first_screen()
    question_number = 0
    data = read_json(json_file=json_path)
    score = 0
    while question_number < len(data):
        question = load_question(data, item=question_number)
        #options_type = question[-1]
        show_question_cli(question, question_number + 1)
        response = verify_answer(question, get_user_choise())
        
        if response == True:
            print('Correto ...')
            score += 1
        else:
            print('Incorreto...')
        #print(len(data))
        question_number += 1
        
        input('Aperte Enter para continuar ou (CTRL + C) para sair')
        
    show_score(score, data)
        
    
# %%
main()
# %%
