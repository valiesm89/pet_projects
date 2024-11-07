'''This is my rock paper scissors game with a GUI through tkinter'''


# dictionary
choices = ['rock','paper','scissor']

# import tkinter lib
from tkinter import *
import random
from PIL import ImageTk, Image

# create an instance of Tk and assign it to root
root = Tk()

root.iconbitmap('icon.PNG')
root.title('Rock Paper Scissors')
root.resizable(width=False, height=False)

# global variable click
click = True

# rock_hand img
rock = PhotoImage(file= 'rock_edi.PNG')

# scissor_hand img
scissor = PhotoImage(file= 'scissor_edi.PNG')

# paper_hand img
paper = PhotoImage(file= 'paper_edi.PNG')

# win img
win_boy = PhotoImage(file= 'win_boy.PNG')

# lose img
lose = PhotoImage(file= 'lose.PNG')

# tie img
tie = PhotoImage(file= 'tie.PNG')

# question mark
img_guess_p = PhotoImage(file='guess_boy.PNG')
img_guess_c = PhotoImage(file = 'guess_computer.PNG')

# comparison operators
img_less = PhotoImage(file= 'less.PNG')
img_greater = PhotoImage(file= 'greater.PNG')
img_equal = PhotoImage(file = 'equal.PNG')
img_comparison = PhotoImage(file= 'comparison.PNG')

# create labels
guessp = Label(root, image= img_guess_p)
guessc = Label(root, image= img_guess_c)
less = Label(root, image= img_less)
greater = Label(root, image= img_greater)
equal = Label(root, image= img_equal)
comparison = Label(root,image= img_comparison)

# button variables
rHbutton = ''
pHbutton = ''
sHbutton = ''

# define functions
def play():
    global rHbutton, pHbutton,sHbutton,guessp, guessc, equal

    rHbutton = Button(root,image= rock, command = lambda:get_user_choice('rock'))
    pHbutton = Button(root,image= paper, command = lambda:get_user_choice('paper'))
    sHbutton = Button(root,image= scissor, command = lambda:get_user_choice('scissor'))


    exitbutton = Button(root, text= 'Exit Game!',height=10, width=20, fg= 'red', command=root.quit)

    rHbutton.grid(row= 0,column=0)
    pHbutton.grid(row=0, column=1)
    sHbutton.grid(row=0, column=2)
    
    guessp.grid(row =2,column=0)
    comparison.grid(row=2, column=1)
    guessc.grid(row =2,column=2)
    
    exitbutton.grid(row=4, column=1)
    

def get_computer_choice():
    comp_choice = random.choice(choices)
    return comp_choice

def get_user_choice(yourchoice):
    global click

    comp_choice = get_computer_choice()
    
    # dictionary to map choices to variables
    choice_images = {
        'rock': rock,
        'paper': paper,
        'scissor': scissor}
    
    if click == True:
        if yourchoice == 'rock':
            guessp.config(image= rock)
            
            if comp_choice == 'rock':
                comparison.config(image= img_equal)                
            
            elif comp_choice == 'paper':
                comparison.config(image= img_less)

            elif comp_choice == 'scissor':
                comparison.config(image= img_greater)

        if yourchoice == 'paper':
            guessp.config(image= paper)
            
            if comp_choice == 'rock':
                comparison.config(image= img_greater)                
            
            elif comp_choice == 'paper':
                comparison.config(image= img_equal)

            elif comp_choice == 'scissor':
                comparison.config(image= img_less)

        if yourchoice == 'scissor':
            guessp.config(image= scissor)

            if comp_choice == 'rock':
                comparison.config(image= img_less)                
            
            elif comp_choice == 'paper':
                comparison.config(image= img_greater)

            elif comp_choice == 'scissor':
                comparison.config(image= img_equal)

        guessc.config(image = choice_images[comp_choice])

                

    # else:
    #     if comp_choice == 'rock' or comp_choice == 'paper' or comp_choice == 'scissor':
    #         rHbutton.configure(image=rock)
    #         pHbutton.configure(image=paper)
    #         sHbutton.configure(image=scissor)
    #         click = True

            
          

# call to game function
play()

# create a window
root.mainloop()

