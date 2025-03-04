# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior que o número sorteado.
# Caso o usuário acerte, dê o parabéns.

from random import randint

def get_random_num() -> int: 
    """Generate a random number"""
    return randint(1, 15)
    
def get_user_guess():
    while True:
        guess = input("Type a number between 1 - 15:\n")
        try:
            guess = int(guess)
            if guess > 0 and guess < 16:
                return guess
            raise ValueError()
        except:
            print("Erro Value: type a number between 1 and 15\n")

def verify_guess(number, guess):
    if number == guess:
        return 'win'
    elif number < guess:
        return 'small'
    else:
        return 'bigger'
    
def main():
    num_guess = 0
    number = get_random_num()
    print(number)
    
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
 
