'''This is my rock paper scissors game'''


""" ##here I will build the functions




##here is the main game, where I will call the functions

#while loop for running game


    #ask for input from user

    #assign selection to computer

    #check if win

    #print result

    #ask if you want to play again. """

#dictionary
choices = {
    'R': 1,
    'P': 2,
    'S': 3
}


# Functions to Build:

    # get_user_choice(): Prompt the user to input their choice (rock, paper, or scissors).

def get_user_choice():
        choice = ''

        while True:
            choice = input('Please enter your choice: R, P or S: \n').upper()
            
            if choice not in ['R', 'P', 'S']:
                print('You did not enter a valid selection! Please enter R, P, S')
                continue
            else:
                 print(f'Thanks, you selected {choice}!\n Let the battle begin!')
                 break
        print(f'Thanks, you selected {choice}, which corresponds to {choices[choice]}!\n Let the battle begin!')
        return choice, choices[choice]  # Return the choice and its corresponding value
    
get_user_choice()    

    # get_computer_choice(): Randomly assign a choice to the computer (using random.choice() on a list of ["rock", "paper", "scissors"]).
import random

def get_computer_choice():
     comp_choice = random.randint(1,3)
     return comp_choice

get_computer_choice()
    

    # determine_winner(user, computer): Compare user and computer choices to determine the result, returning "win", "lose", or "tie".
    # display_result(winner): Show the outcome based on the result from determine_winner().
    # play_again(): Prompt to check if the user wants to play another round.

# Game Loop:

    # Set up a while loop that calls these functions in the correct order:
    # Get user input.
    # Generate computer choice.
    # Check who won using determine_winner().
    # Display the outcome.
    # Ask if the player wants to continue; if not, break the loop.