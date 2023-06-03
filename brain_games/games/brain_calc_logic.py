from brain_games.logic_for_all_games.all_logic import greeting, \
    user_input, add_counter, generate_expression, evaluate_expression


def do_brain_calc_game(counter: int):
    """ game_logic
    """
    usr_name = greeting()
    rules = 'What is the result of the expression?'
    print(rules)
    while True:
        expression = generate_expression()
        question = f'Question: {expression}'
        print(question)
        user_input_answer = user_input()
        try:
            user_input_answer = int(user_input_answer)
        except Exception:
            print('Incorect input. Please input inly num\'s value')
            continue
        correct_answer = evaluate_expression(expression)
        if user_input_answer == correct_answer:
            print('Correct!')
            counter = add_counter(counter)
        else:
            computer_answer = (f"'{user_input_answer}' is wrong answer ;(."
                               f"Correct answer was '{correct_answer}'."
                               f"\nLet's try again, {usr_name}!")
            print(computer_answer)
            break
        if counter == 3:
            print(f'Congratulations, {usr_name}!')
            break


def run():
    """Running function do_brain_calc_game"""
    do_brain_calc_game(0)
