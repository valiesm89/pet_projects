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
        #img_guess_p = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'guess_boy.PNG'))
    else:
        rock = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'rock_emma.PNG'))
        paper = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'paper_emma.PNG'))
        scissor = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'scissor_emma.PNG'))
        #img_guess_p = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'guess_girl.PNG'))

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


init_screen()