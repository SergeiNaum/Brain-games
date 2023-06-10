import math
from random import randint

"""Brain Prime Game."""

DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 65


def is_prime(digit: int) -> str:
    """used to calculate a prime digit"""
    if digit < 2:
        return 'no'
    for d in range(2, int(math.sqrt(digit)) + 1):
        if digit % d == 0:
            return 'no'
    return 'yes'



def make_question_and_correct_answer():
    """Make game question and answer."""
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    return question, is_prime(number)
