'''
10.1 Escreva uma função chamada nested_sum que receba uma lista de números inteiros
e adicione os elementos de todas as litas aninhadas
Ex: lista = [[1,2], 3, [4,5,6]]
'''
def nested_sum(list):
    soma = 0
    for indice, numero in enumerate(list):
        for interno in list[indice]:

            soma += interno
    return soma

lista = [[1,2], [3], [8,5,6]]
matriz = [
    [1, 8, 2],
    [10, 3, 4],
    [6, 5, 9],
]


print(nested_sum(lista))
print(nested_sum(matriz))
