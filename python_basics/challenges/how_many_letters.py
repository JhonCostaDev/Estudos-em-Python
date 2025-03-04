# Faça um programa que conte quantas vezes a letra 'a' aparece em uma palavra

#%%
word = 'pindamonhagaba'
user_letter = 'A'
count = 0
for letter in word.lower():
    if user_letter.lower() == letter.lower():
        count += 1

count

# %%
