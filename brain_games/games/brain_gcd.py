"""Brain-GCD Game."""

from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 99


def make_question_and_correct_answer():
    """Make game question and answer."""
    number_first = randint(MIN_NUMBER, MAX_NUMBER)
    number_second = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number_first} {number_second}'
    correct_answer = gcd(number_first, number_second)
    return question, str(correct_answer)
