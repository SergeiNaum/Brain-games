"""Brain-Even Game."""

from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 99


def iseven(num: int) -> bool:
    ''' This function checking is num % 2 == 0 or not
    '''
    flag = False
    if num % 2 == 0:
        flag = True
    return flag


def make_question_and_correct_answer():
    """Make game question and answer."""
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    if iseven(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
