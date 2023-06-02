from logic_for_all_games.all_logic import greeting, iseven, user_input, add_counter, randint


def do_brain_even_game(counter):
    ''' game_logic
    '''
    usr_name = greeting()
    rools = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(rools)
    while True:
        random_num = randint(1, 15)
        question = f'Question: {random_num}'
        print(question)
        num = iseven(random_num)
        user_input_answer = user_input()
        if num and (user_input_answer == 'yes'):
            computer_answer = 'Correct!'
            counter = add_counter(counter)
        elif not num and (user_input_answer == 'no'):
            computer_answer = 'Correct!'
            counter = add_counter(counter)
        elif not num and (user_input_answer == 'yes'):
            computer_answer = (f"'{user_input_answer}' is wrong answer ;(."
                               f"Correct answer was 'no'.\nLet's try again, {usr_name}!")
        else:
            computer_answer = (f"'no' is wrong answer ;(. Correct answer was 'yes'.\n"
                               f"Let's try again, {usr_name}!")
        print(computer_answer)
        if counter == 3:
            print(f'Congratulations, {usr_name}!')
            break


def run():
    do_brain_even_game(0)
