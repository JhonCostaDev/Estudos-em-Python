# Considere a lista:
# lista = [120, "Python", 120.1, "asw", False, [10, 20]]
# Faça um programa que retorne as seguintes informações:
#   * Elemento na última posição da lista
#   * Elemento na primeira posiçãp da lista
#   * O último caractere do segundo elemento da lista. 

#%%
lista = [120, "Python", 120.1, "asw", False, [10, 20]]

# Ultimo elemento
lista[-1]
# %%
# Primeiro elemento
lista[0]
# %%
# Último caractere do segundo elemento da lista
lista[-1][-1] = str(lista[-1][-1])
# %%
int(lista[-1][-1][-1])
# %%
