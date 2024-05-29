'''
10.3 - Escreva uma função chamada middle que receba uma lista e retorne uma nova
lista com todos os elementos originais, exceto o primeiro e o último elemento!
'''
def middle(list):
    list.pop(0)
    list.pop()
    return list
numeros = [1, 2, 3, 4]
frutas = ["laranja", "maçã", "uva", "pêra", "goiaba"]
print(middle(numeros))
print(middle(frutas))

