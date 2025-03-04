# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas

#%%
sum = 0

for i in range(4):
    sum += float(input(f'Type the {i + 1} height:\n'))
    print(sum)

sum

# %%
