'''This is my rock paper scissors game with a GUI through tkinter'''


# dictionary
choices = ['rock','paper','scissor']

# import tkinter lib
from tkinter import *
import random
from PIL import ImageTk, Image
from tkinter import font
import os

# create an instance of Tk and assign it to root
root = Tk()

icon_path = os.path.join(os.path.dirname(__file__), 'icon.PNG')

root.iconbitmap(os.path.join(os.path.dirname(__file__), 'icon.PNG'))
root.title(os.path.join(os.path.dirname(__file__), 'Rock Paper Scissors'))
root.resizable(width=False, height=False)

# global variable click
click = True

# rock_hand img
rock = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'rock_edi.PNG'))

# scissor_hand img
scissor = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'scissor_edi.PNG'))

# paper_hand img
paper = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'paper_edi.PNG'))

# win img
win_boy = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'win_boy.PNG'))

# lose img
lose = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'lose.PNG'))

# tie img
tie = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'tie.PNG'))

# question mark
img_guess_p = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'guess_boy.PNG'))
img_guess_c = PhotoImage(file = os.path.join(os.path.dirname(__file__), 'guess_computer.PNG'))

# comparison operators
img_less = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'less.PNG'))
img_greater = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'greater.PNG'))
img_equal = PhotoImage(file = os.path.join(os.path.dirname(__file__), 'equal.PNG'))
img_comparison = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'comparison.PNG'))

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

    # define custom font
    custom_font = font.Font(family="Helvetica", size=16, weight="bold")

    # create title label
    title_label = Label(root, text="Pick: Rock, Paper or Scissor", font=custom_font, fg="blue")
    title_label.grid(row=0, column=0, columnspan=3, pady=10)

    # create subtitle label
    subtitle_label = Label(root, text="Your choice vs. Computer choice:", font=custom_font, fg="blue")
    subtitle_label.grid(row=2, column=1, columnspan=3, sticky=W, padx=10)

    # create subtitle label
    subtitle_label = Label(root, text="Emma & Edi", font=custom_font, fg="blue")
    subtitle_label.grid(row=4, column=0, columnspan=3, sticky=W, padx=10)

    # create subtitle label
    subtitle_label = Label(root, text="Computer", font=custom_font, fg="green")
    subtitle_label.grid(row=4, column=2, columnspan=3, sticky=W, padx=10)

    rHbutton = Button(root,image= rock, command = lambda:get_user_choice('rock'))
    pHbutton = Button(root,image= paper, command = lambda:get_user_choice('paper'))
    sHbutton = Button(root,image= scissor, command = lambda:get_user_choice('scissor'))


    exitbutton = Button(root, text= 'Exit Game!',height=10, width=20, fg= 'red', command=root.quit)

    rHbutton.grid(row= 1,column=0)
    pHbutton.grid(row=1, column=1)
    sHbutton.grid(row=1, column=2)
    
    guessp.grid(row =3,column=0)
    comparison.grid(row=3, column=1)
    guessc.grid(row =3,column=2)
    
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

