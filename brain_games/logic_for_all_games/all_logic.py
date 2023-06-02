from random import randint, choice

import prompt


def greeting() -> str:
	'''function print Hello, { inputing name } and return user_name
	'''
	user_name = prompt.string('May I have your name? ')
	print(f'Hello, {user_name}')
	return user_name


def iseven(num: int) -> bool:
	''' This function checking is num % 2 == 0 or not
	'''
	flag = False
	if num % 2 == 0:
		flag = True
	return flag


def validation(value):
	if type(value) != type(int):
		return print('Incorect input. Please input inly num\'s value')
	else:
		return value


def user_input() -> str:
	inp = prompt.string('Your answer: ')
	return inp


def add_counter(current_counter: int) -> int:
	current_counter += 1
	return current_counter


def generate_expression(max_value=100):
	math_action_lst = ['+', '-', '*']

	random_num1 = randint(1, max_value)
	random_num2 = randint(1, max_value)
	math_action = choice(math_action_lst)

	expression = f"{random_num1} {math_action} {random_num2}"
	return expression


def evaluate_expression(expression) -> int or float:
	return eval(expression)


def gcd(a: int, b: int) -> int:
	while b:
		a, b = b, a % b
	return a


def generate_arithm_progression(min_length=5, max_length=10) -> list:
	length = randint(min_length, max_length)
	start = randint(1, 10)
	step = randint(1, 5)
	progression = [start + i * step for i in range(length)]
	return progression


def hide_element(progression: list) -> tuple:
	hidden_index = randint(0, len(progression) - 1)
	hidden_element = progression[hidden_index]
	progression[hidden_index] = ".."
	return hidden_element, progression


def isprime(digit: int) -> bool:
	d = 2
	while d * d <= digit and digit % d != 0:
		d += 1
		return d * d > digit


def computer_wrong_answer(user_answer, user_name):
	message = (f"'{user_answer}' is wrong answer ;(."
                 f"Correct answer was 'no'.\nLet's try again, {user_name}!")
	return message