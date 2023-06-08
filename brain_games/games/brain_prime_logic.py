from brain_games.logic_for_all_games.all_logic import is_prime
from random import randint

"""Brain Prime Game."""

DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'


def make_question_and_correct_answer():
    """Make game question and answer."""
    min_number = 1
    max_number = 21
    number = randint(min_number, max_number)
    question = str(number)
    return question, is_prime(number)
