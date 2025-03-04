# Faça um programa que receba uma quantidade indefinida de valores correspondentes a 'saldo em conta', mas quando o usuário apertar 'enter' sem digitar valor algum, o programa para de receber valores e exibe a soma de todos os valores digitados...

#%%
sum_balance = 0


while True:
    balance = input("Type the balance\n")
    if balance == "":
        break
    sum_balance += float(balance)

print(sum_balance)