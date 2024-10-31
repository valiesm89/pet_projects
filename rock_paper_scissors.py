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
choices = ['R','P','S']


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
                 print(f'Thanks, you selected {choice}!\nLet the battle begin!')
                 break
        return choice
    
    # get_computer_choice(): Randomly assign a choice to the computer (using random.choice() on a list of ["rock", "paper", "scissors"]).
import random

def get_computer_choice():
     comp_choice = random.choice(choices)
     return comp_choice
   

    # determine_winner(user, computer): Compare user and computer choices to determine the result, returning "win", "lose", or "tie".

def determine_winner(user, computer):
    if user == 'R' and computer == 'S':
        print(f'You Won with your choice: {user} against computer choice: {computer}')
    elif user == 'P' and computer == 'R':
        print(f'You Won with your choice: {user} against computer choice: {computer}')
    elif user == 'S' and computer == 'P':
        print(f'You Won with your choice: {user} against computer choice: {computer}')
    elif user == computer:
        print(f'You guys tied with your choice: {user} against computer choice: {computer}!!!')
    else:
        print(f'You lost with your choice: {user} against computer choice: {computer}')

    return user, computer

    # display_result(winner): Show the outcome based on the result from determine_winner().
    ##skip for now as I built the logic into the above but I would write win, lose, tie and fix that to a variable such as result
    ##Then I would call the result, user and computer to the display_result function
     

    # play_again(): Prompt to check if the user wants to play another round.
def play_again():
    while True:
        answer = input('Do you want to play again? "Y" or "N"? \n').upper()
        if answer == 'Y':
            return True
        elif answer == 'N':
            return False
        else:
            print('You did not enter a valid value')
            
             
        # # # # #more elegant from chatgpt
        # # # # #      # play_again(): Prompt to check if the user wants to play again.
        # # # # # def play_again():
        # # # # #     return input('Do you want to play again? "Y" or "N"? \n').upper() == 'Y'




# Game Loop:

while True:
    # Get user input.
    user_choice = get_user_choice()

    # Generate computer choice.
    computer_choice = get_computer_choice()

    # Check who won using determine_winner().
    determine_winner(user_choice, computer_choice)

    # Display the outcome.
    ##Skipped for now as it is integrated in determine_winner()

    #check if player wants to continue
    if not play_again():
        print('Thanks for playing! See you next time.')
        break    
