from brain_games.logic_for_all_games.all_logic import \
    greeting, isprime, user_input, add_counter, randint,\
    is_correct_answer, wrong_answer


def do_brain_prime_game(counter: int):
    """ game_logic
    """
    usr_name = greeting()
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    print(rules)
    while True:
        random_num = randint(1, 150)
        question = f'Question: {random_num}'
        print(question)
        num = isprime(random_num)
        user_input_a = user_input()
        if is_correct_answer(num, user_input_a):
            counter = add_counter(counter)
            print('Correct!')
        else:
            computer_answer = wrong_answer(num, user_input_a, usr_name)
            print(computer_answer)
            break
        if counter == 3:
            print(f'Congratulations, {usr_name}!')
            break


def run():
    """Running function do_brain_prime_game"""
    do_brain_prime_game(0)
