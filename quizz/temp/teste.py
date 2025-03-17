print('oi')
tamanho = 3

letra = 'a'
tags = 'a'
for i in range(1, tamanho + 1):
	tags += chr(ord(letra) + i).upper()

# chr(ord(letra) + 2)
for letra in tags:
	print(letra)