'''This is my rock paper scissors game with a GUI through tkinter'''


# dictionary
choices = ['rock','paper','scissor']

# import tkinter lib
from tkinter import *
import random

# create an instance of Tk and assign it to root
root = Tk()

root.iconbitmap('C:\\PORTABLE\\repos\\rock_paper_scissors\\Game\\icon.PNG')
root.title('Rock Paper Scissors')
root.resizable(width=False, height=False)

# global variable click
click = True

# rock_hand img
rock = PhotoImage(file= 'C:\\PORTABLE\\repos\\rock_paper_scissors\\Game\\rock_edi.PNG')

# scissor_hand img
scissor = PhotoImage(file= 'C:\\PORTABLE\\repos\\rock_paper_scissors\\Game\\scissor_edi.PNG')

# paper_hand img
paper = PhotoImage(file= 'C:\\PORTABLE\\repos\\rock_paper_scissors\\Game\\paper_edi.PNG')

# win img
win_boy = PhotoImage(file= 'C:\\PORTABLE\\repos\\rock_paper_scissors\\Game\\win_boy.PNG')
win_girl = PhotoImage(file= 'C:\\PORTABLE\\repos\\rock_paper_scissors\\Game\\win_girl.PNG')

# lose img
lose = PhotoImage(file= 'C:\\PORTABLE\\repos\\rock_paper_scissors\\Game\\lose.PNG')

# tie img
tie = PhotoImage(file= 'C:\\PORTABLE\\repos\\rock_paper_scissors\\Game\\tie.PNG')

# button variables
rHbutton = ''
pHbutton = ''
sHbutton = ''

# define functions
def play():
    global rHbutton, pHbutton,sHbutton

    rHbutton = Button(root,image= rock, command = lambda:youPick('rock'))
    pHbutton = Button(root,image= paper, command = lambda:youPick('paper'))
    sHbutton = Button(root,image= scissor, command = lambda:youPick('scissor'))

    rHbutton.grid(row= 0,column=0)
    pHbutton.grid(row=0, column=1)
    sHbutton.grid(row=0, column=2)
    

def get_computer_choice():
    comp_choice = random.choice(choices)
    return comp_choice

def get_user_choice():
    global click

    comp_choice = get_computer_choice()
    
    if click == True:
        pass
    else:
        if comp_choice == 'rock' or comp_choice == 'paper' or comp_choice == 'scissor':
            rHbutton.configure(image=rock)
            pHbutton.configure(image=paper)
            sHbutton.configure(image=scissor)
            click = True

          
    
          


play()

# create a window
root.mainloop()

