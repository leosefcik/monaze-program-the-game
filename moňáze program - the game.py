import os
import random
from datetime import datetime
global state
state=0
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def menu():
    clear()
    splash=random.randrange(0,5)
    print(" /$$      /$$                                                  ")
    print("| $$$    /$$$               ˇ          ´                       ")
    print("| $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$  /$$$$$$ ")
    print("| $$ $$/$$ $$ /$$__  $$| $$__  $$ |____  $$|____ /$$/ /$$__  $$")
    print("| $$  $$$| $$| $$  \ $$| $$  \ $$  /$$$$$$$   /$$$$/ | $$$$$$$$")
    print("| $$\  $ | $$| $$  | $$| $$  | $$ /$$__  $$  /$$__/  | $$_____/")
    print("| $$ \/  | $$|  $$$$$$/| $$  | $$|  $$$$$$$ /$$$$$$$$|  $$$$$$$")
    print("|__/     |__/ \______/ |__/  |__/ \_______/|________/ \_______/")
    print(" ")
    print("   /$$     /$$                ")
    print("  | $$    | $$                ")
    print(" /$$$$$$  | $$$$$$$   /$$$$$$ ")
    print("|_  $$_/  | $$__  $$ /$$__  $$")
    print("  | $$    | $$  \ $$| $$$$$$$$")
    print("  | $$ /$$| $$  | $$| $$_____/")
    print("  |  $$$$/| $$  | $$|  $$$$$$$")
    print("   \___/  |__/  |__/ \_______/")
    print(" ")
    print("  /$$$$$$                                   ")
    print(" /$$__  $$                                  ")
    print("| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ ")
    print("| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$")
    print("| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$")
    print("| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/")
    print("|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$")
    print(" \______/  \_______/|__/ |__/ |__/ \_______/")
    print(" ")
    if splash==0:
        print("Pro tip: play in fullscreen for extra immersion!")
    if splash==1:
        print("Be sure to check out Moňáze Program (the original)!")
    if splash==2:
        print("Baba booey")
    if splash==3:
        print("This splash has a 1 in 5 chance to show up!")
    if splash==4:
        print("banan still cost 20 money :O")
    print("\nEnter 1 to play\nEnter 2 to do something else idk really\n")
    choice=input(":: ")
    global state
    if choice=="1":
        state=1
    elif choice=="2":
        state=3
def tutorial():
    input("Here will be tutorial lol")
    global state
    state=0
def difficulty():
    clear()
    global dif
    dif=input("\n1: Easy (Really easy)\n2: Normal (Recommended)\n3: Hard (Nightmarish)\nChoose your difficulty: ")
    global state
    global difp
    global difm
    if dif=="1":
        state=2
        difp=1.25
        difm=0.75
    if dif=="2":
        state=2
        difp=1
        difm=1
    if dif=="3":
        state=2
        difp=0.75
        difm=1.25
def gamesetup():
    global money
    global happiness
    global reputation
    global health
    money=random.randrange(100*difp,200*difp)
    happiness=50
    reputation=50
    health=100
    global loss
    loss=0
    global state
    state=4
    global raund
    raund=0
def game():
    clear()
    global money
    global happiness
    global reputation
    global health
    global loss
    global state
    global raund
    
    print("\nRound      |",raund)
    print("\nMoney      |",money)
    print("Happiness  |",happiness)
    print("Reputation |",reputation)
    print("Health     |",health)
    print(" ")
    global yn
    yn=input(":: ")
def gameover():
    clear()
    input("\nYou ded lol\npress any key to continue")
    global state
    state=0
while True:
    if state==0:
        menu()
    if state==3:
        tutorial()
    if state==1:
        difficulty()
    if state==2:
        gamesetup()
    if state==4:
        game()
        
        raund=raund+1
        happiness=happiness-1*difm
        
        if happiness<=0:
            loss=1
        if money<=0:
            loss=1
        if reputation<=0:
            loss=1
        if reputation<=0:
            loss=1
        if loss==1:
            state=5
            
    if state==5:
        gameover()