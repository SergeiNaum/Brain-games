#!/usr/bin/env python
"""Brain-Even Game start."""


from brain_games.engine import run_game
from brain_games.games import even_logic


def main():
    """Start the "Brain-Even Game"."""
    run_game(even_logic)


if __name__ == '__main__':
    main()
