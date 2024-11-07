'''This is my rock paper scissors game for Emma and Edi'''

# dictionary
choices = ['R','P','S']


# functions to Build:

# get_user_choice(): Prompt the user to input their choice (rock, paper, or scissors).
def get_user_choice():
        player_name = ''
        choice = ''

        while True:
            # first deal with asking for the player
            player_name = input('Who is playing? Please enter "Emma" or "Edi": \n').lower()
            
            if player_name not in ['emma', 'edi']:
                print('You are not allowed to play. This game is only for Emma and Edi!')
                continue
            else:
                print(f'Hi {player_name.capitalize()}, good luck!')
            
            # second ask for their choice    
            choice = input('Please enter your choice: R, P or S: \n').upper()

            if choice not in ['R', 'P', 'S']:
                print('You did not enter a valid selection! Please enter R, P, S')
                continue
            else:
                 print(f'Thanks, you selected {choice}! yLet the battle begin!')
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


# Game Loop:
while True:
    # Get user input.
    user_choice = get_user_choice()

    # Generate computer choice.
    computer_choice = get_computer_choice()

    # Check who won using determine_winner().
    determine_winner(user_choice, computer_choice)

    #check if player wants to continue
    if not play_again():
        print('Thanks for playing! See you next time.')
        break    
