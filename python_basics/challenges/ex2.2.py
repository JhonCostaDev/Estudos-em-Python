#%%
def par_impar(number:int):
    """Verifica se um número é par ou ímpar"""
    if number % 2 == 0:
        print('par!')
    else:
        print('impar!')
        
numero = input("Type a number\n")
numero = int(numero)
par_impar(number=numero)
# %%
