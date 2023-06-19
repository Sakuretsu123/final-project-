#!python3
import tkinter as tk
import math 
import random 
import getpass
import time 




window = tk.Tk()
window.title('final project')
window.geometry('600x200')
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

#how to hide the character of a password
'''
password = getpass.getpass()
print(password)
mypass = getpass.getpass("PASSWORD : ")
'''

lives1 = 3
lives2 = 3
p1 = None
p2 = None
ready_ = False 
gameState = 0
x, y = None, None
"""
0 - getting names
1 - first decision
"""


def ready(e): 
    global ready_
    ready_ = True 
    game1(e)


def names():
    global player1, player2
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
    global p1, p2
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

def decision(e): 
    x=0
    while x == 0:
        label1 = tk.Label(window,text="make a decision", bg="#FFFFFF")
        label1.grid(row=0,column=0)
        if e.keysym == "Left":
            x = 1
            return 0
        if e.keysym == "Right":
            x = 1
            return 1

def updateWindow():
    global lives1, lives2
    if x != None and y != None: 
        if x == 0 and  y == 0:
            lives1 += 1
            lives2 += 1
        if x == 0 and y == 1: 
            lives1 -= 1
        if x == 1 and y == 0: 
            lives2 -= 1
        if x == 1 and y == 1:  
            lives1 -= 1
            lives2 -= 1
    if gameState == 0 or gameState ==2 or gameState ==4:
        label3 = tk.Label(window,text=f"{p1} press the arrow key corresponding to your decision \n(either left for negociate of right for betray) ", bg="#FFFFFF")
        label3.grid(row=0,column=0)
        window.bind("<KeyPress>",gameKey1)
    if gameState == 1 or  gameState ==3 or gameState ==5:
        label3 = tk.Label(window,text=f"{p2} press the arrow key corresponding to your decision \n(either left for negociate of right for betray)")
        label3.grid(row=0,column=0)
        window.bind("<KeyPress>",gameKey2)

    if gameState == 6: 
        print( x, y)
        if lives1 == 0 or lives2 == 0: 
            gamestop()
        else: 
            gameon()
       
def gamestop(): 
    print("bruh")

def gameon():
    print("yipee")


def gameKey1(e):
    print(e)
    global gameState, x
    x = 0
    if e.keysym=="Left":
        gameState += 1
        window.unbind("<KeyPress>")
        x = 0
        for widget in window.winfo_children():
            widget.destroy()
    elif e.keysym == "Right":
        gameState +=1
        x = 1
        window.unbind("<KeyPress>")
    print(gameState)
    updateWindow()

    
def gameKey2(e):
    print(e)
    global gameState, y
    y = 0
    if e.keysym=="Left":
        gameState += 1
        window.unbind("<KeyPress>")
        y = 0
        for widget in window.winfo_children():
            widget.destroy()
    elif e.keysym == "Right":
        gameState +=1
        y = 1
        window.unbind("<KeyPress>")
    print(gameState)
    updateWindow()

def game1(e): 
    global myList
    myList = []
    playtime = 3
    while ready_== True and playtime !=0: 
        print("Game1 while")
        for widget in window.winfo_children():
        #    if someKeyPressed:
            widget.destroy()
        playtime -=1
        updateWindow()
        #myList.append( decision(e) )
        #for widget in window.winfo_children():
        #    widget.destroy()

        
        #label4 = tk.Label(window,text=f"{p2} press the arrow key corresponding to your decision \n(either left for negociate of right for betray) ", bg="#FFFFFF")
        #label4.grid(row=0,column=0)
        #decision(e)
        #print("worked")
        #time.sleep(2)
       

        #for widget in window.winfo_children():
        #    widget.destroy()

        """
        if myList[0] == 0 and myList[1] == 0:
            lives1 += 1
            lives2 += 1
        if myList[0] == 0 and myList[1] == 1: 
            lives1 -= 1
        if myList[0] == 1 and myList[1] == 0: 
            lives2 -= 1
        if myList[0] == 1 and myList[1] == 1:  
            lives1 -= 1
            lives2 -= 1
        """



names()



window.mainloop()