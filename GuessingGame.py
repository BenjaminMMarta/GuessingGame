#--Imports--#
import random

#--Global variables--#
#Generate random number between 1 and 10.
random_number = random.randint(1,10)
#Player guesses begin at 0 with each new game.
player_guesses = 0
#Maximum number of guesses allowed for each game.
maximum_guesses = 10
player_guess = int(input("Can you guess the number I picked between 1 and 10?\n"))
#--Guessing Game Logic--#
while player_guesses < maximum_guesses:
    try:
        #print(f"You guessed: {player_guess}")
        if player_guess < random_number:
            player_guess = int(input(f"That's too low! You have {maximum_guesses - player_guesses} more {'guesses' if maximum_guesses - player_guesses > 1 else 'guess'}. Try again.\n\n"))
        elif player_guess > random_number:
            player_guess = int(input(f"That's too high! You have {maximum_guesses - player_guesses} more {'guesses' if maximum_guesses - player_guesses > 1 else 'guess'}. Try again.\n\n"))
        else:
            #Displays "attempt" or "attempts" depending player_guesses value.
            print(f"Correct! You guessed the secret number in {player_guesses + 1} {'attempts' if player_guesses + 1 > 1 else 'attempt'}.")
            break
    
        #Add 1 when player guesses incorrectly.
        player_guesses += 1 
        #Display message with remaining guesses.
        #player_guess = int(input(f"Pick another number! Guesses remaining: {maximum_guesses - player_guesses}.\n\n"))
    except ValueError:
        print("Invalid input! Please enter a valid number.")

#Display message stating random number when player runs out of guesses.
if player_guesses >= maximum_guesses:
    print(f"Sorry, you're out of guesses. The correct number was {random_number}!")
    