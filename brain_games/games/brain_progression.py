"""Brain Progression Game."""
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def hide_element(progression: list) -> tuple:
    """used to hide element in the list"""
    hidden_index = randint(0, len(progression) - 1)
    hidden_element = progression[hidden_index]
    progression[hidden_index] = ".."
    return hidden_element, progression


def generate_progression(min_length=5, max_length=10) -> list:
    """used to generate math progression"""
    length = randint(min_length, max_length)
    start = randint(1, 10)
    step = randint(1, 5)
    progression = [start + i * step for i in range(length)]
    return progression


def make_question_and_correct_answer():
    """ Make game question and answer."""
    progression = generate_progression()
    correct_answer, progression = hide_element(progression)
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
