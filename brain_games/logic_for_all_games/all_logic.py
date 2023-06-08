import math
import prompt
from random import randint


def greeting() -> str:
    '''function print Hello, { inputing name } and return user_name
    '''
    print("Welcome to the Brain Games!")
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


def generate_progression(min_length=5, max_length=10) -> list:
    """used to generate math progression"""
    length = randint(min_length, max_length)
    start = randint(1, 10)
    step = randint(1, 5)
    progression = [start + i * step for i in range(length)]
    return progression


def hide_element(progression: list) -> tuple:
    """used to hide element in the list"""
    hidden_index = randint(0, len(progression) - 1)
    hidden_element = progression[hidden_index]
    progression[hidden_index] = ".."
    return hidden_element, progression


def is_prime(digit: int) -> str:
    """used to calculate a prime digit"""
    if digit < 2:
        return 'no'
    for d in range(2, int(math.sqrt(digit)) + 1):
        if digit % d == 0:
            return 'no'
    return 'yes'
