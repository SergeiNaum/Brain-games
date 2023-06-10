#!/usr/bin/env python
"""Brain Prime Game start."""


from brain_games.engine import run_game
from brain_games.games import brain_prime


def main():
    """Start the "Brain-Prime Game"."""
    run_game(brain_prime)


if __name__ == '__main__':
    main()
