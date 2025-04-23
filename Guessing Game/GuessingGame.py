#-----Imports-----#
import random

#-----Global Variables-----#
#Generate random number between 1 and 10.
random_number = random.randint(1,10)
#Player guesses begins at 0 with each new game.
player_guesses = 0
#Maximum number of guesses allowed for each game.
maximum_guesses = 10
#Initial player guess.
player_guess = int(input("I'm thinking of a number between 1 and 10! Can you guess it?\n"))

#-----Guessing Game Logic-----#
#While loop when player guesses is less than maximum guesses.
while player_guesses < maximum_guesses:
    try:
        if player_guess < random_number:
            player_guess = int(input(f"That's too low! You have {maximum_guesses - player_guesses} more {'guesses' if maximum_guesses - player_guesses > 1 else 'guess'}. Please try again.\n\n"))
        elif player_guess > random_number:
            player_guess = int(input(f"That's too high! You have {maximum_guesses - player_guesses} more {'guesses' if maximum_guesses - player_guesses > 1 else 'guess'}. Please try again.\n\n"))
        else:
            #Display "attempt" or "attempts" depending on number of player guesses remaining.
            print(f"Correct! You guessed the secret number in {player_guesses + 1} {'attempts' if player_guesses + 1 > 1 else 'attempt'}.")
            break
    
        #Add 1 when player guesses incorrectly.
        player_guesses += 1 

    #Display message when player enters value other than valid number.   
    except ValueError:
        print("Invalid input! Please enter a valid number.")

#Display message when player runs out of guesses.
if player_guesses >= maximum_guesses:
    print(f"Sorry, you're out of guesses. The correct number was {random_number}!")
    