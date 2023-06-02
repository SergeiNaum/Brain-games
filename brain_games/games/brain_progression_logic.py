from brain_games.logic_for_all_games.all_logic import \
    greeting, user_input, add_counter, generate_arithm_progression, hide_element


def do_brain_progression_game(counter):
    ''' game_logic
    '''
    usr_name = greeting()
    rools = 'What number is missing in the progression?'
    print(rools)
    while True:
        hidden_element, progression = hide_element(generate_arithm_progression())
        print("Question:", " ".join(str(x) for x in progression))
        answer = user_input()
        try:
            answer = int(answer)
        except Exception:
            print('Incorect input, please input only digits')
            continue

        if answer == hidden_element:
            counter = add_counter(counter)
            print("Correct!")
        else:
            computer_answer = (f"'{answer}' is wrong answer ;(."
                               f"Correct answer was '{hidden_element}'."
                               f"\nLet's try again, {usr_name}!")
            print(computer_answer)
        if counter == 3:
            print(f'Congratulations, {usr_name}!')
            break


def run():
    do_brain_progression_game(0)
