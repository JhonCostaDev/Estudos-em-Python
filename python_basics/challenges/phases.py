'''
2.18
Escreva um programa que solicite ao usuário frases. Para parar de solicitar frases, ele pode apenas apertar o enter.
seu programa deve apresentar cada frase e quantas vezes ela foi repetida
'''
phrases = {} # to store

while True:     # while loop
    user_phrase = input('Type a phrase\n').capitalize() #user input

    if bool(user_phrase) == False:      #verify if user type something
        for key, value in phrases.items():  # show the phrases
            print(f'{key}: {value}')
        break                               #exit loop
    
    if user_phrase in phrases:              # verify if phrases alreary in dictionary
        phrases[user_phrase] += 1           # add 1 
    else:
        phrases[user_phrase] = 1            # add new key value to the dicitionary


