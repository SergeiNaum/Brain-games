"""Engine for all Brain Games."""
import prompt


MAX_ROUND = 3


def greeting() -> str:
    '''function print Hello, { inputing name } and return user_name
    '''
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}')
    return user_name


def run_game(game_name):
    """Run Brain Games."""
    user_name = greeting()
    print(game_name.DESCRIPTION)

    for round_number in range(MAX_ROUND):
        question, correct_answer = game_name.make_question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if not (user_answer == correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {user_name}!")
            return
        print("Correct!")
    else:
        print(f"Congratulations, {user_name}!")
