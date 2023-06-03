import prompt


def welcome_user() -> str:
    """function return Hello, { inputing name }
    """
    username = prompt.string('May I have your name? ')
    return f'Hello, {username}'
