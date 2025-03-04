# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior que o número sorteado.
# Caso o usuário acerte, dê o parabéns.

from random import randint

def get_user_guess()->int:
    """Get user's guess"""
    while True:
        guess = input("Type a number between 1 - 15:\n") # ask the guess
        try:                                             # to validate the entry
            guess = int(guess)                           # trying convert to int
            if guess > 0 and guess < 16:                 # verify if the number is between 1 - 15
                return guess                             # return the integer number
            raise ValueError()
        except:                     # If it can't convert raise a erro
            print("Erro Value: type a number between 1 and 15\n")

def verify_guess(number, guess) -> str:
    """Check if the numbers are equal"""
    if number == guess:
        return 'win'
    elif number < guess:
        return 'small'
    else:
        return 'bigger'
    
def main():
    num_guess = 0           # 
    number = randint(1, 15) # Generate random number
   
    while num_guess < 4:
        num_guess += 1
        user_guess = get_user_guess()

        result = verify_guess(number, user_guess)

        if result == 'win':
            print(f'Congratulation, you find a secret number with {num_guess} guess!')
            break
        elif result == 'small':
            print("The secret number is smaller than the guess")
        else:
            print("The secret number is bigger than the guess")



main()
 
