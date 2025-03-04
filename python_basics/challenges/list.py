# Escreva um programa que receba uma lista de números do usuário e conte quantas vezes um número específico aparece na lista.
# Solicite ao usuário o número e exiba a contagem

# gerar lista
#%%
from random import randint

random_numbers = [randint(1,100) for _ in range(100)]
numbers = [1, 2, 2, 3, 4,4,4, 5, 6, 7,7, 7,6]
#user = int(input("Type a number"))

count = 0

# if user in random_numbers:
#     count += 1
#%%
random_numbers.count(38)
numbers.count(4)


# %%
