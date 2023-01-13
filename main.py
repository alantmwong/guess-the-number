#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

# The random number for a user to guess
random_number = random.randint(1, 100)


def determine_starting_attempts():
    """Allows player to set difficulty to determine starting attempts"""
    game_difficulty = input(
        "Which level difficulty do you want to play?: Type 'easy' or 'hard'")
    if game_difficulty == "easy":
        attempts_remaining = 10
    elif game_difficulty == "hard":
        attempts_remaining = 5

    return attempts_remaining


def play_game():
    attempts_remaining = determine_starting_attempts()

    game_over = False

    while game_over == False:

        if attempts_remaining < 1:
            game_over = True
