#%%
binary = ''
number = 1

if number == 0:
    binary = str(number)
else:
    while number > 0:
        binary += str(number % 2)
        number //=  2


result = int(binary[::-1])
result
# %%
