#!/usr/bin/env python
"""Brain-GCD Game start."""


from brain_games.engine import run_game
from brain_games.games import brain_gcd_logic


def main():
    """Start the "Brain-GCD Game"."""
    run_game(brain_gcd_logic)


if __name__ == '__main__':
    main()
