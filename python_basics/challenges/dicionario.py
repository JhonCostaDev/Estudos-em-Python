'''EX 2.7
Escreva um programa que crie um dicionário com nomes de frutas como chaves e seus respectivos preços como valores. Solicite so usuário  o nome de uma fruta e exiba o preço correspondente.
'''
#%%
fruits = ['apple', 'banana', 'grape', 'pear', 'orange', 'lemon', 'guava', 'pineapple', 'jackfruit']

fruits_values = [1.5, 2.75, 1.9, 1.25, 0.65, 1.25, 2.15, 3.20, 5.8]


# %%
dict_fruits = {}

for i in range(len(fruits)):
    dict_fruits[fruits[i]] = fruits_values[i]
    
dict_fruits
# %%
user = input("Which fruit do you want?\n").lower()

print(dict_fruits.get(user))
# %%

# sum fruits values

sum(dict_fruits.values())
# %%
# Average of values

sum(dict_fruits.values())/len(dict_fruits.values())
# %%

#min
min(dict_fruits.values())
# %%
#Max
max(dict_fruits.values())
# %%
