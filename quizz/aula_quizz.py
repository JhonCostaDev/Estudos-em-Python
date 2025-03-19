import json
import textwrap

file_path = 'correct_quiz_raw.json'

def load_json(json_file) -> dict:
	"""Essa função carrega o arquivo json e retorna um dicionário"""
	with open(json_file, mode='r', encoding='utf-8') as file:
		data = json.load(file)
		return data


# carregar a pergunta
def load_question(dictionary):
	question = dictionary.get('question')
	options = dictionary.get('options')
	answer = dictionary.get('correct_answer')
	return question, options, answer


# exibir no cli
def show_question_cli(dictionary:dict) -> None:
	max_width = 70

	question_options = load_question(dictionary)
	question = textwrap.fill(question_options[0], width=max_width)
	options = question_options[1]
	len_options = len(question_options[1]) 
	letter = 'A'
	tags = ''
	# gerar tags 
	for i in range(len_options + 1):
		tags += chr(ord(letter) + i).upper()
	# answer = tuple[2]

	print(f'\n{question}\n')
	for index, option in enumerate(options):
		print(f'{tags[index]}) {textwrap.fill(option, width=max_width)}')

# Validar resposta
def verify_entry(dictionary, user_answer):
	data = load_question(dictionary)
	len_options = len(data[1])
	letter = 'A'
	tags = []
	
	for i in range(len_options):
		tags.append(chr(ord(letter) + i).upper())
	print(tags)

	if user_answer in tags:
		return user_answer
	else:
		return False
# Pegar resposta do usuario

def get_answer(dictionary):
	data = load_question(dictionary)
	len_options = len(data[1])
	answer = data[-1]
	type_asnwer = type(answer).__name__
	#construir a tag verificadora de acordo com o tamanho das opcoes
	
	
	#print(tags)
	if type_asnwer == 'list':
		user_answer = []
		for i in range(len(answer)):
			user_answer.append(input(f'Digite a resposta {i + 1}\n'))
		print(len_options)
		return user_answer
	else:
		user_answer = input('Digite a resposta')
		print(len_options)
		return user_answer
	

	

# Verificar restposta

def verify_answer(dictionary, user_answer=0):
	data = load_question(dictionary)
	options = data[1]
	answer = data[-1]
	type_asnwer = type(answer).__name__
	print(options)

	if type_asnwer == 'list':
		pass

data = load_json(file_path)[17]

show_question_cli(data)
# #verify_answer(data)
# print(get_answer(data))
#validate_user_answer(data)
