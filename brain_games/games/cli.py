import prompt


def welcome_user() -> str:
    """function return Hello, { inputting name }
    """
    username = prompt.string('May I have your name? ')
    return f'Hello, {username}'
