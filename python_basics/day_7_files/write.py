file_name = 'My history.txt'

text = 'Água. Terra. Fogo. Ar. Há muito tempo, as quatro nações viviam em harmonia, mas tudo mudou quando a Nação do Fogo atacou. Só o Avatar, mestre dos quatro elementos, poderia detê-los, mas quando o mundo mais precisava dele, ele desapareceu. Cem anos se passaram e a Nação do Fogo está prestes a vencer a guerra. Duas jovens da Tribo da Água do Sul encontraram o novo Avatar, um dominador de ar chamado Aang. E embora sua habilidade de dominar o ar seja ótima, ele tem muito a aprender antes de poder salvar alguém. Mas eu acredito que Aang pode salvar o mundo.'

eng_text = 'Water, earth, fire, air. There are long time, the four nations lived in peace and harmony. But everything change when the fire nation attack. Only the avatar ...'


eng_text_2 = '\n\nI forgot the space'
# Write
#with open(file_name, mode='w') as file:
    #file.write(text)


# Add new rows
with open(file_name, mode='a') as file:
    file.write(eng_text_2)
