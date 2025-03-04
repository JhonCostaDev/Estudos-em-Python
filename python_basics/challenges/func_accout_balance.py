# Faça um programa que receba uma quantidade indefinida de valores correspondentes a 'saldo em conta', mas quando o usuário apertar 'enter' sem digitar valor algum, o programa para de receber valores e exibe a soma de todos os valores digitados...

#%%
print("Please, enter the values, when you finish just type Enter.\n")
account_balance = 0

def user_value() -> float:
    value = input("Please enter the value\n")

    try:
        value = float(value)
        if value < 0:
            print("Error: enter a number greater than zero")
            user_value()

        return value
    except ValueError:
        print("Error: Entrada inválida. Digite um número inteiro.")
        user_value()

def sum_balance() -> float:
    value =  user_value()
    sum = 0
    while bool(value) == True:
        sum += value

    return sum


print(bool(user_value()))