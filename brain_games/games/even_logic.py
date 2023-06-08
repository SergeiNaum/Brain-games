"""Brain-Even Game."""

from random import randint
from brain_games.logic_for_all_games.all_logic import iseven

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question_and_correct_answer():
    """Make game question and answer."""
    min_number = 1
    max_number = 99
    number = randint(min_number, max_number)
    question = str(number)
    if iseven(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
