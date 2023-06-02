import prompt
from random import randint, choice


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


def evaluate_expression(expression):
    return eval(expression)


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def arithm_progression():
    length = randint(5, 10)
    start = randint(1, 100)  # начальный элемент
    diff = randint(1, 10)  # разность прогрессии
    seq = [start]  # добавляем начальный элемент в последовательность

    for i in range(length - 1):  # заполняем последовательность до нужной длины
        seq.append(seq[-1] + diff)
    return seq
