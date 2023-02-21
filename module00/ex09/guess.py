import sys
import random


def guess(min, max):
    if min > max:
        tmp = min
        min = max
        max = tmp
    to_guess = random.randint(min, max)
    player_trials = 0
    player_guess = min - 1

    print(
        f'This is an interactive guessing game!\n'
        f'You have to enter a number between {min} and {max}'
        f'to find out the secret number.\n'
        f'Type "exit" to end the game.\n'
        f'Good luck!'
    )
    while player_guess != to_guess:
        player_guess = input(f"\nWhat's your guess between {min} and {max}?\n")
        player_trials += 1
        if player_guess == "exit":
            print("Goodbye!")
            return
        try:
            player_guess = int(player_guess)
        except ValueError:
            print("That's not a number.")
            player_guess = min - 1
            continue
        if player_guess > to_guess:
            print("Too high!")
        if player_guess < to_guess:
            print("Too low!")
        if player_guess == to_guess:
            if player_trials == 1:
                print("Whaou first try! Take a cookie.")
            if to_guess == 42:
                print(
                    f'The answer to the ultimate question of life,'
                    f' the universe and everything.'
                )
            print(
                f'Congratulations, you\'ve got it!\n'
                f'You won in {player_trials} attempts!'
            )
            return


if __name__ == "__main__":
    guess(1, 99)
