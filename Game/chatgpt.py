'''This is my rock paper scissors game with a GUI through tkinter'''

# dictionary
choices = ['rock', 'paper', 'scissor']

# import tkinter lib
from tkinter import *
import random
from PIL import ImageTk, Image
from tkinter import font
import os

                         
# create an instance of Tk and assign it to root
root = Tk()
root.iconbitmap(os.path.join(os.path.dirname(__file__), 'icon.PNG'))
root.title('Rock Paper Scissors')  # Changed title to a string directly
root.resizable(width=False, height=False)

# global variable click
click = True
selected_gender = 'boy'

# button variables
rHbutton = ''
pHbutton = ''
sHbutton = ''

# create labels
guessp = Label(root)
guessc = Label(root)
less = Label(root)
greater = Label(root)
equal = Label(root)
comparison = Label(root)

# load gender images
def load_images(gender):
    global rock, paper, scissor, img_guess_p, img_guess_c
    if gender == 'boy':
        rock = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'rock_edi.PNG'))
        paper = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'paper_edi.PNG'))
        scissor = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'scissor_edi.PNG'))
        img_guess_p = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'guess_boy.PNG'))
    else:
        rock = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'rock_emma.PNG'))
        paper = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'paper_emma.PNG'))
        scissor = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'scissor_emma.PNG'))
        img_guess_p = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'guess_girl.PNG'))

    # global images
    img_guess_c = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'guess_computer.PNG'))

# comparison operators
def load_comp_imgs():
    global img_less, img_greater, img_equal, img_comparison
    img_less = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'less.PNG'))
    img_greater = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'greater.PNG'))
    img_equal = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'equal.PNG'))
    img_comparison = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'comparison.PNG'))

# init screen
def init_screen():
    global pick_girl, pick_boy

    pick_boy = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'superhero_boy.PNG'))
    pick_girl = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'superhero_girl.PNG'))

    # clear
    for widget in root.winfo_children():
        widget.destroy()

    # label and button
    welcome_label = Label(root, text="Choose a Character", font=("Helvetica", 18))
    welcome_label.pack(pady=20)

    boy_button = Button(root, image=pick_boy, command=lambda: start_game("boy"))
    girl_button = Button(root, image=pick_girl, command=lambda: start_game("girl"))

    boy_button.pack(side=LEFT, padx=20)
    girl_button.pack(side=RIGHT, padx=20)

# start game with gender adjusted imgs
def start_game(gender):
    global selected_gender
    selected_gender = gender
    load_images(gender)
    load_comp_imgs()
    game_screen()

# game screen function
def game_screen():
    global rHbutton, pHbutton, sHbutton, guessp, guessc, equal

    # clear screen
    for widget in root.winfo_children():
        widget.destroy()

    # set up game layout
    play()

# # define functions
# def play():
#     global rHbutton, pHbutton, sHbutton, guessp, guessc, equal, comparison

#     # define custom font
#     custom_font = font.Font(family="Helvetica", size=16, weight="bold")

#     # create title label
#     title_label = Label(root, text="Pick: Rock, Paper or Scissor", font=custom_font, fg="blue")
#     title_label.grid(row=0, column=0, columnspan=3, pady=10)

#     # create subtitle label
#     subtitle_label = Label(root, text="Your choice vs. Computer choice:", font=custom_font, fg="blue")
#     subtitle_label.grid(row=2, column=1, columnspan=3, sticky=W, padx=10)

#     # create subtitle label
#     subtitle_label = Label(root, text="Emma & Edi", font=custom_font, fg="blue")
#     subtitle_label.grid(row=4, column=0, columnspan=3, sticky=W, padx=10)

#     # create subtitle label
#     subtitle_label = Label(root, text="Computer", font=custom_font, fg="green")
#     subtitle_label.grid(row=4, column=2, columnspan=3, sticky=W, padx=10)

#     # buttons
#     rHbutton = Button(root, image=rock, command=lambda: get_user_choice('rock'))
#     pHbutton = Button(root, image=paper, command=lambda: get_user_choice('paper'))
#     sHbutton = Button(root, image=scissor, command=lambda: get_user_choice('scissor'))
#     exitbutton = Button(root, text='Exit Game!', height=10, width=20, fg='red', command=root.quit)

#     # place buttons
#     rHbutton.grid(row=1, column=0)
#     pHbutton.grid(row=1, column=1)
#     sHbutton.grid(row=1, column=2)

#     # Update labels with images
#     guessp.config(image=img_guess_p)
#     guessc.config(image=img_guess_c)
#     less.config(image=img_less)
#     greater.config(image=img_greater)
#     equal.config(image=img_equal)
#     comparison.config(image=img_comparison)

#     guessp.grid(row=3, column=0)
#     comparison.grid(row=3, column=1)
#     guessc.grid(row=3, column=2)

#     exitbutton.grid(row=4, column=1)

# def get_computer_choice():
#     comp_choice = random.choice(choices)
#     return comp_choice

# def get_user_choice(yourchoice):
#     global click

#     comp_choice = get_computer_choice()

#     # dictionary to map choices to variables
#     choice_images = {
#         'rock': rock,
#         'paper': paper,
#         'scissor': scissor}

#     if click:
#         if yourchoice == 'rock':
#             guessp.config(image=rock)

#             if comp_choice == 'rock':
#                 comparison.config(image=img_equal)
#             elif comp_choice == 'paper':
#                 comparison.config(image=img_less)
#             elif comp_choice == 'scissor':
#                 comparison.config(image=img_greater)

#         elif yourchoice == 'paper':
#             guessp.config(image=paper)

#             if comp_choice == 'rock':
#                 comparison.config(image=img_greater)
#             elif comp_choice == 'paper':
#                 comparison.config(image=img_equal)
#             elif comp_choice == 'scissor':
#                 comparison.config(image=img_less)

#         elif yourchoice == 'scissor':
#             guessp.config(image=scissor)

#             if comp_choice == 'rock':
#                 comparison.config(image=img_less)
#             elif comp_choice == 'paper':
#                 comparison.config(image=img_greater)
#             elif comp_choice == 'scissor':
#                 comparison.config(image=img_equal)

#         guessc.config(image=choice_images[comp_choice])

# call for init_screen
init_screen()

# create a window
root.mainloop()