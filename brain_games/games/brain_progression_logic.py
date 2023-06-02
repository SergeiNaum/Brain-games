from brain_games.logic_for_all_games.all_logic import \
    greeting, user_input, add_counter, arithm_progression, randint


def do_brain_progression_game(counter):
    ''' game_logic
    '''
    usr_name = greeting()
    rools = 'What number is missing in the progression?'
    print(rools)
    while True:
        progression = arithm_progression()
        indx = randint(0, len(progression) - 1)
        progression[indx] = '..'
        question = f'Question: {progression}'
        print(question)
        correct_answer = progression[indx]
        user_input_answer = user_input()
        try:
            user_input_answer = int(user_input_answer)
        except Exception:
            print('Incorect input. Please input inly num\'s value')
            continue
        progression[indx] = user_input_answer
        if indx == len(progression) - 1:
            correct_answer = progression[indx - 1] <= user_input_answer
        else:
            correct_answer = progression[indx - 1] <= user_input_answer <= progression[indx + 1]
        if correct_answer:
            computer_answer = 'Correct!'
            counter = add_counter(counter)
        else:
            answer = progression[indx + 1] - 3 if indx > 0 else progression[indx]-3
            computer_answer = (f"'{user_input_answer}' is wrong answer ;(."
                                f"Correct answer was '{answer}'."
                                f"\nLet's try again, {usr_name}!")
        print(computer_answer)
        if counter == 3:
            print(f'Congratulations, {usr_name}!')
            break


def run():
    do_brain_progression_game(0)
