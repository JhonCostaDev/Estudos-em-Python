# ask user which multiplication table he wants to see

multiplication = int(input('Which multiplication table do you want to see?\n'))

# what is the result

# number X int 1 - 9 = result

for i in range(1, 11):
    print(f'{multiplication} X {i} = {multiplication * i}' ) 

