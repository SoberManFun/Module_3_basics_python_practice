#___________________МОДУЛЬ_3_ЧАСТЬ_4_УРОВЕНЬ1_НАЧАЛО____________________
import os.path
import json
#___________________МОДУЛЬ_3_ЧАСТЬ_4_УРОВЕНЬ2_НАЧАЛО____________________
def check_user(login):
	filename = 'users.json'

	if os.path.isfile(filename):
		with open(filename, 'r') as file:
			data = json.load(file)
			for user in data:
				if user['login'] == login:
					return True
	return False
#___________________МОДУЛЬ_3_ЧАСТЬ_4_УРОВЕНЬ2_КОНЕЦ____________________
def register(login, passwd):
	if check_user(login):
		print('Пользователь', login, ' уже существует!')
		return
#__________ДАННЫЕ ХРАНИМ В СПИСКЕ ИЗ СЛОВАРЕЙ С КЛЮЧАМИ 'login' И 'pswrd'
	user = {
		'login': login,
		'pswrd': passwd
	}

	filename = 'users.json'

	if not os.path.isfile(filename):
		with open(filename, 'w') as file:
			json.dump([], file)

	with open(filename, 'r') as file:
		data = json.load(file)

	data.append(user)

	with open(filename, 'w') as file:
		json.dump(data, file)

	print('Пользователь', login, ' зарегистрирован!')

#___________________МОДУЛЬ_3_ЧАСТЬ_4_УРОВЕНЬ3_НАЧАЛО_____________________
def login_function(login, passwd):
	with open('users.json', 'r') as file:
		data = json.load(file)

	for user in data:
		if user['login'] == login and user['pswrd'] == passwd:
			print('Вход пользователя', login, ' выполнен успешно!')
			return
	print('Неправильный логин или пароль!')
#___________________МОДУЛЬ_3_ЧАСТЬ_4_УРОВЕНЬ3_КОНЕЦ_____________________

choice = input('Введите: 1, если хотите войти или: 2, если хотите зарегистрировать нового пользователя ')
if choice == '1':
	login = input('Введите логин: ')
	passwd = input('Введите пароль: ')
	login_function(login, passwd)
elif choice == '2':
	login = input('Введите логин: ')
	passwd = input('Введите пароль: ')
	register(login, passwd)
#___________________МОДУЛЬ_3_ЧАСТЬ_4_УРОВЕНЬ1_КОНЕЦ_____________________
