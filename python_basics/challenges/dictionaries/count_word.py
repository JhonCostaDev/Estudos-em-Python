# Crie um dicionário que conte a frequência de cada palavra em um texto fornecid0 pelo usuario.
#%%%
camoes = "As armas e os barões assinalados, Que da ocidental praia Lusitana Por mares nunca de antes navegados Passaram ainda além da Taprobana, Em perigos e guerras esforçados Mais do que prometia a força humana, E entre gente remota edificaram Novo Reino, que tanto sublimaram; E também as memórias gloriosas Daqueles Reis que foram dilatando A Fé, o Império, e as terras viciosas De África e de Ásia andaram devastando; E aqueles que por obras valerosas Se vão da lei da Morte libertando; Cantando espalharei por toda parte, Se a tanto me ajudar o engenho e arte."

#%%

def count_words_in_a_text(text: str) -> dict:
    """
    This function takes a text/string and it count how many time each word appears in this text. So it save each this word as the key and each count as the value in a dictionary.
    
    """
    dictionary = {}
    list_text = text.lower().split(' ')
    
    for word in list_text:
        if len(word) ==1:
            continue
        
        count = list_text.count(word)
        dictionary[word] = count
    
    return dictionary
            
    

# %%

# %%
count_words_in_a_text(camoes)

# %%
