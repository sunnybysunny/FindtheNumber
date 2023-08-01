import random

from art import LOGO

# constant variables
EASY = 10
HARD = 5

# Helper functions


def check_difficulty():
    """ this function checks the difficulty level selected by user """
    difficulty = input("Choose a diffulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return EASY
    if difficulty == "hard":
        return HARD


def check_user_answer(guess, answer, lives):
    """ this function compares the user answer to the actual answer """
    if guess == answer:
        print("You win, you guessed the number!")
        return
    if guess < answer:
        print("Too low.")
        return lives - 1
    if guess > answer:
        print("Too high.")
        return lives - 1


def find_the_number():
    print(LOGO)
    random_num = random.randint(1, 100)
    print("Welcome to the Find the Number guessing game!\nI'm thinking of a number between 1 and 100.")
    lives = check_difficulty()

    while lives:
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        lives = check_user_answer(guess, random_num, lives)
        if lives == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != random_num:
            print("Guess again.")


find_the_number()
