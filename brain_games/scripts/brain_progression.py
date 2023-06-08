#!/usr/bin/env python
"""Brain Progression Game start."""


from brain_games.engine import run_game
from brain_games.games import brain_progression_logic


def main():
    """Start the "Brain-Progression Game"."""
    run_game(brain_progression_logic)


if __name__ == '__main__':
    main()
