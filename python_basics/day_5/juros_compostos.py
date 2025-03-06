#%%
def juros_compostos(aporte:int, taxa:float, anos:int)-> float:
    '''Juros compostos servem para calcular o retorno financeiro a partir de um aporte. Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para cálculo do valor a ser retornado.
    
    aporte: Um número inteiro, que represente o valor em R$
    
    Taxa: Um número float entre 0 e 1 que representa o valor taxa de juros
    
    anos: Um número inteiro  >= 1 que representa o tempo que o investimento terá para ser liquidado.
    '''
    return aporte * (1 + taxa) ** anos 
    
    
juros_compostos(aporte=1000, taxa=0.13, anos=4)

# %%
