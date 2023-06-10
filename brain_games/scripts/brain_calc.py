#!/usr/bin/env python
"""Brain-Calc Game start."""


from brain_games.engine import run_game
from brain_games.games import brain_calc


def main():
    """Start the "Brain-Calc Game"."""
    run_game(brain_calc)


if __name__ == '__main__':
    main()
