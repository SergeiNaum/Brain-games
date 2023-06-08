"""Brain Progression Game."""

from brain_games.logic_for_all_games.all_logic import generate_progression,\
    hide_element

DESCRIPTION = 'What number is missing in the progression?'


def make_question_and_correct_answer():
    """ Make game question and answer."""
    progression = generate_progression()
    correct_answer, progression = hide_element(progression)
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
