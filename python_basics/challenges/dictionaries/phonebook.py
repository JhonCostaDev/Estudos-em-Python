'''
Agenda Telefônica:

* Crie um dicionário que armazene nomes e números de telefone.
* Permita que o usuário adicione, remova e consulte números de telefone.
'''
import os
import time
import json
import re


def load_json(data_path):
    print(data_path)
    if os.path.isfile(data_path):
        print('Existe')
        with open(data_path, 'r', encoding='utf-8') as file:
            content = json.load(file)
            
            return content
    else:
        print('Criando arquivo')
        dictionary = dict()
        with open(data_path, mode='w') as file:
            json.dump(dictionary, file, indent=4)
            
def save_json(file_path, dictionary):
    with open(file_path, 'w') as file:
        json.dump(dictionary, file, indent=4)

#contacts = {}
def take_option():
    while True:
        option = input()
        try:
            option = int(option)
            if option in [0, 1, 2, 3, 4]:
                return option
            else:
                raise ValueError
        except ValueError:
            print('Option Incorrect, type the correct option!')
            time.sleep(1.5)
            show_menu()
            
    
    
def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('     ====== Phonebook ====== ')
    print("""
    Press [1] To show all contacts
    Press [2] To find a contact
    Press [3] To Registre new contact
    Press [4] To remove a contact
    Press [0] to Exit .
    
    """)
    
def show_all_contacts(dictionary):
    #print('show all')
    if not dictionary:
        print('The phonebook is empty')
    
    print('NAME\tNUMBER')
    for key, value in dictionary.items():
        print(f'{key}\t-->\t{value}')

def validate_phone_number():
    padrao = r"^\(?(\d{2})\)?\s?(\d{4,5})-?(\d{4})$"
    while True:
        number = input(f'Type the number for new contact\n')
        match = re.match(padrao, number)
        
        if match:
            ddd, prefix, p_number = match.groups()
            return f'({ddd} {prefix}-{p_number})'
        else:
            print('Invalid Phone Number\nTry again!')

def add_contact(dictionary):
    
    new_contact = input("Type the name\n").lower()
    if new_contact in dictionary:
        print(f"{new_contact} it's already in the phonebook")
    
    number = validate_phone_number()
    
    dictionary[new_contact] = number
    print('Contact added')
    

def find_contact(dictionary):
    if not dictionary:
        print('The phonebook is empty')
    contact = input("Type the name\n").lower()
    
    if contact not in dictionary:
        print('Name not found')
    else:
        number = dictionary.get(contact)
        print(f'{contact}\t{number}')
    
    

def remove_contact(dictionary):
    print('remove')
    

def main():
    data_path = 'python_basics/challenges/dictionaries/data/contacts.json'
    
    contacts = load_json(data_path=data_path)
    print(contacts)
    while True:
        show_menu()
        option = take_option()
        
        if option == 1:
            print('======================')
            show_all_contacts(contacts)
            input('======================\nType any key to continue ...')
            
        elif option == 2:
            find_contact(contacts)
            input('======================\nType any key to continue ...')
        elif option == 3:
            add_contact(contacts)
            time.sleep(2)
        elif option == 4:
            remove_contact(contacts)
            time.sleep(2)
        else:
            print('Saving phonebook')
            save_json(data_path, contacts)
            time.sleep(2)
            break
        
    
#===========================================    
main()