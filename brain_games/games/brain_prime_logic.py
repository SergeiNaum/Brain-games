from brain_games.logic_for_all_games.all_logic import \
    greeting, isprime, user_input, add_counter, randint, computer_wrong_answer


def do_brain_even_game(counter):
    ''' game_logic
    '''
    usr_name = greeting()
    rools = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    print(rools)
    while True:
        random_num = randint(1, 150)
        question = f'Question: {random_num}'
        print(question)
        num = isprime(random_num)
        user_input_answer = user_input()
        # computer_wrong_answer = (f"'{user_input_answer}' is wrong answer ;(."
        #                    f"Correct answer was 'no'.\nLet's try again, {usr_name}!")
        if num and (user_input_answer == 'yes'):
            computer_answer = 'Correct!'
            counter = add_counter(counter)
        elif not num and (user_input_answer == 'no'):
            computer_answer = 'Correct!'
            counter = add_counter(counter)
        elif not num and (user_input_answer == 'yes'):
            computer_answer = computer_wrong_answer(user_input_answer, usr_name)
        else:
            computer_answer = computer_wrong_answer(user_input_answer, usr_name)
        print(computer_answer)
        if counter == 3:
            print(f'Congratulations, {usr_name}!')
            break


def run():
    do_brain_even_game(0)
