#!/usr/bin/env python
"""Brain-Even Game start."""


from brain_games.engine import run_game
from brain_games.games import brain_even


def main():
    """Start the "Brain-Even Game"."""
    run_game(brain_even)


if __name__ == '__main__':
    main()
