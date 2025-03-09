file_name = 'data.csv'

with open(file_name) as file:
    content = file.readlines()

for linha in content:
    print(linha
    )