import json
import os


file_path = 'json/review_cap1.json'

def first_screen():
    #exibir menu inicial
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
{'#'* 149}
|
|                                                           SIMULADO AWS
|                                                           70 QUESTÕES
|
{'#'* 149}
''')
    input("Presione Enter para iniciar ...")

def load_and_convert_json_to_dict(json_file) -> dict:
    """Carrega um arquivo JSON, transforma em um dicionario python."""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def load_question(dictionary, chapter=0, list_position=0) -> dict:
    """Select one question of dictionary"""
    key = list(dictionary.keys())[chapter]
    list_lenght = len(dictionary[key]) # tamanho 
    list_questions = dictionary[key]

    return list_questions[list_position]

#print(type(load_question(load_and_convert_json_to_dict(file_path),0,0)['answer']).__name__ == 'str')

def show_question(dictionary):
    '''Show the question in CLI'''
    question_number = dictionary['questionNumber']
    question = dictionary['questionText']
    dict_options = dictionary['options']
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=' * 100)
    print(dictionary['questionText'])
    print('=' * 100)
    for tag, option in dict_options.items():
        print(f'({tag}): {option}')
    print('=' * 100)


def get_user_choise():
    """Take the user option"""
    valid_options = ['A', 'B', 'C', 'D']
    while True:
        user_choise = input('Type your answer\n').upper()
        if user_choise in valid_options:
            return user_choise
        print('Invalid option, please choise A, B, C, and D')
    
    
#validate answer

def check_answer(user_answer, selected_question):
    """Check the correct answer"""
    asnwer = user_answer
    question = selected_question['options']
    correct_answer = selected_question['answer']
    type_answer = type(selected_question['answer']).__name__
    #print(type_answer)
    print(correct_answer) # TODO: implement this
    if type_answer != 'str':
        pass
    
    
    if question[asnwer] == correct_answer:
        return True
    else:
        return False
    
    
def show_result(user_answer, chapter=0, question_number=0) -> None:
    """Show the result to user"""
    data = load_and_convert_json_to_dict(file_path)
    question = load_question(data, chapter, question_number)
    explanation = question["explanation"]
    
    if check_answer(user_answer, question):
        print('=' * 100)
        print("Correct")
        print('=' * 100)
        print(f'Explanation:\n{explanation}')
        print('=' * 100)
            
    else:
        print('=' * 100)
        print("Incorrect")
        print('=' * 100)
        print(f'Explanation:\n{explanation}')
        print('=' * 100)

def main():
    """Main function"""
    first_screen()
    score = 0 # TODO: Fix it
    chapter = 0
    question_number = 0
    data = load_and_convert_json_to_dict(file_path)
    lenght_dict = len(list(data.keys()))
    
    
    while chapter < lenght_dict:
        print(question_number)
        key = list(data.keys())[chapter]
        leght_questions =len(data[key])
        question = load_question(data, chapter, question_number)
        show_question(question)
        answer = get_user_choise()
        
        if check_answer == True:
            score += 1
        
        show_result(answer, chapter, question_number)
        question_number += 1
        
        if question_number == leght_questions:
            question_number = 0
            chapter += 1
        input('Press any key to going to the next question\n')
        
        
        
    print(score) # TODO: improve this

main()

# NEXT STEP, CLEAN SCREEN,
# STOP UNTIL USER TYPE SOMETHING TO THE NEXT QUESTION










