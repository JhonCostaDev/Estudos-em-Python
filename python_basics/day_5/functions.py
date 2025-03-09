#%%
a = 2
a
# %%
data = {
    'pergunta': 'qual a fruta',
    'opcoes': {
        'a': 'goiaba',
        'b': 'maca',
        'c': 'laranja',
        'd': 'limao'
    },
    'resposta': 'goiaba'
}
# %%
reposta = 'b'
# %%
data['pergunta']#.get(reposta) #== data['restosta']
# %%
data['resposta']
# %%
data['opcoes'].get(reposta) == data['resposta']
# %%
