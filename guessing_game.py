"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    print(' \nWELCOME TO THE: Number Guessing Game\n')
    print('------------------------------------------\n')

    attempts = 0
    highscore = None
    startgame = True

    while True:

        if startgame:
            number_to_guess = random.choice(range(1, 11))
            startgame = False
            if highscore:
                print('\nHighscore is {}.\n'.format(highscore))

        # check if input is number
        try:
            guess = int(input('Guess the number between 1 and 10:'))
        except:
            print('Only numbers are allowed!')
            continue

        # check guess out of range
        if guess < 1 or guess > 10:
            print('The number is between 1 and 10. Try again!')
            continue

        # check guess
        attempts += 1

        if guess < number_to_guess:
            print('''It's higher.''')
        elif guess > number_to_guess:
            print('''It's lower.''')
        else:
            print('You guessed the correct number! ({})'.format(number_to_guess))

            # play again
            again = input('Whould you like to play again? y/n :')
            if again.lower() == 'y':
                if highscore == None:
                    highscore = attempts
                elif highscore > attempts:
                    highscore = attempts
                attempts = 0
                startgame = True
                continue
            else:
                break


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
