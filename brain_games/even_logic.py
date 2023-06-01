import prompt
from random import randint


def welcome_user() -> str:
    '''function return Hello, { inputing name }
    '''
    username = prompt.string('May I have your name? ')
    return username


def iseven(num: int) -> bool:
    ''' This function checking is num % 2 == 0 or not
    '''
    flag = False
    if num % 2 == 0:
        flag = True
    return flag


# def validation(*args):
#     lst = [str(x) for x in range(1, 16)]
#     if args in lst:
#         return True
#     elif args not in lst:
#         return False


def user_input():
    inp = prompt.string('Your answer: ')
    return inp


def game_logic():
    ''' game_logic
    '''
    usr_name = welcome_user()
    print(f'Hello, {usr_name}')
    counter = 0
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
            counter += 1
        elif not num and (user_input_answer == 'no'):
            computer_answer = 'Correct!'
            counter += 1
        else:
            computer_answer = "'yes' is wrong answer ;(. Correct answer \\" \
                                "was 'no'.\nLet's try again, Bill!"
        print(computer_answer)
        if counter == 3:
            print(f'Congratulations, {usr_name}!')
            break
