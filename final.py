#!python3
import tkinter as tk
import math 
import random 




window = tk.Tk()
window.title('')
window.geometry('400x200')
'''
I would like to create a two players game that allows two variables to be input. 
Negotiate and Report. 

Ask the player's name ? 

My program will ask each player if they want to either Negociate or report. 
If they both negotiate they both get one life 
If they both report they both lose one life 
If one report and one negotiate the player negotiating lose one life 

They both start with two lives,
After 3 turns, the players will have the opportunity to answer a math question randomly generated one at a time, if they get 
it wrong they lose one extra life. 
If one player falls to 0 life, they lose 

After those two minigames, the player with the most lives wins. 

-----------------------------------------------------------------------------------------------------------------------

Use the name input and use it all the way through the program --> done 
Minigame n*1(accepting input and reacting accordingly) 
minigame n*2 (generating two math questions and their answers)
Gestion of the players lives 
Reboot so that it keeps playing until exit 

Maybe displaying it in a window with tkinter (if time) ?

Maybe displaying a winner screen (if time) ? 
Maybe displaying a tie screen (if time) ? 
'''



lives1 = 3
lives2 = 3

ready_ = False 



def ready(): 
    global ready_
    ready_ = True 

def names():
    global player1
    global player2
    namelabel1 = tk.Label(window,text="What is the name of player 1 ?", bg="#FFFFFF")
    namelabel1.grid(row=0,column=0)
    namelabel2 = tk.Label(window,text="What is the name of player 2 ?", bg="#FFFFFF")
    namelabel2.grid(row=1,column=0)
    player1 = tk.Entry(window, width=40)
    player1.grid(row=0,column=1)
    player2 = tk.Entry(window, width=40)
    player2.grid(row=1,column=1)

    b1 = tk.Button(window,text="confirm")
    b1.grid(row=3,columnspan=2)
    b1.bind("<Button-1>",play)
    
    
def play(e):
    p1 = player1.get()
    p2 = player2.get()
    if player1.get() != "" and player2.get() != "": 
        for widget in window.winfo_children():
            widget.destroy()
        label1 = tk.Label(window,text=f"Welcome to the prisoner's dilemna,{p1} and {p2}\n in this game you will have to type once at a time the letter corresponding to your choice, do not let the other player know which option you picked as it is a bluffing game", bg="#FFFFFF")
        label1.grid(row=0,column=0)
        label2 = tk.Label(window,text="Now let's learn the rules together, you are two villain in jail that are trying to escape.\n You will have the choice between negociating with your partner or betray them. if you both choose to negociate, \n then both players win one life, if one choose to negociate and the other to betray, the player that gets betrayed lose one life. if you both report then both of you lose one life \nafter 3 turns, you will have the opportunity to answer a math question,\nif you get it right the other player lose one life, the game stops when one or both players reach 0 hp \n", bg="#FFFFFF")
        label2.grid(row=1,column=0)
        b1 = tk.Button(window,text="ready ?")
        b1.grid(row=5,columnspan=2)
        b1.bind("<Button-1>",ready)
    else: 
        names()

names()

window.mainloop()