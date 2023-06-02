from logic_for_all_games.all_logic import greeting,  user_input, add_counter, generate_expression, evaluate_expression, validation



def do_brain_calc_game(counter):
    ''' game_logic
    '''
    usr_name = greeting()
    rools = 'What is the result of the expression?'
    print(rools)
    while True:
        expression = generate_expression()
        question = f'Question: {expression}'
        print(question)
        try:
            user_input_answer = int(user_input())
            correct_answer = evaluate_expression(expression)
        except:
            print('Incorect input. Please input inly num\'s value')
        if user_input_answer == correct_answer:
            computer_answer = 'Correct!'
            counter = add_counter(counter)
        else:
            computer_answer = (f"'{user_input_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                               f"Let's try again, {usr_name}!")
        print(computer_answer)
        if counter == 3:
            print(f'Congratulations, {usr_name}!')
            break


def run():
    do_brain_calc_game(0)
