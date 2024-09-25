from tkinter import *
from tkinter import messagebox
from random import choice

window=Tk()
window.geometry("300x300")
window.title("Rock paper scissor game")

choices=["rock","paper","scissor"]

def game(userchoice):
    computer_choice= choice(choices)
    result=""

    if userchoice == computer_choice:
        result="It is a tie!"
    elif(userchoice=="rock"and computer_choice=="scissor"):
        result="You win!"
    elif(userchoice=="scissor"and computer_choice=="paper"):
        result="You win!"
    elif(userchoice=="paper"and computer_choice=="rock"):
        result="You win!"
    else:
        result="You lose!"

    messagebox.showinfo("Result","Your choice:"+ userchoice + "\nComputer's choice:"+ computer_choice +"\n\n" +result )
#buttons
rock_button=Button(window,text="Rock",command=lambda:game("rock"))
rock_button.pack()
scissor_button=Button(window,text="Scissor",command=lambda:game("scissor"))
scissor_button.pack()
paper_button=Button(window,text="Paper",command=lambda:game("paper"))
paper_button.pack()


window.mainloop()