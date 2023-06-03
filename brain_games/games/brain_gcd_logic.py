from brain_games.logic_for_all_games.all_logic import \
    greeting, user_input, add_counter, randint, gcd


def do_brain_gcd_game(counter: int):
    """ game_logic
    """
    usr_name = greeting()
    rules = 'Find the greatest common divisor of given numbers.'
    print(rules)
    while True:
        random_num1 = randint(1, 100)
        random_num2 = randint(1, 100)
        question = f'Question: {random_num1} {random_num2}'
        print(question)
        user_input_answer = user_input()
        try:
            user_input_answer = int(user_input_answer)
        except Exception:
            print('Incorect input. Please input inly num\'s value')
            continue
        correct_answer = gcd(random_num1, random_num2)
        if user_input_answer == correct_answer:
            computer_answer = 'Correct!'
            counter = add_counter(counter)
        else:
            computer_answer = (f"'{user_input_answer}' is wrong answer ;(."
                               f"Correct answer was '{correct_answer}'."
                               f"\nLet's try again, {usr_name}!")
        print(computer_answer)
        if counter == 3:
            print(f'Congratulations, {usr_name}!')
            break


def run():
    """Running function do_brain_gcd_game"""
    do_brain_gcd_game(0)
