import random
import sys
import time


name = input("Please, write your name: ")

def play_information():
    print("""
          Hello this is my first Py project
             Rock Papper Scissors
                 r for rock
                 p for papper
                 s for scossors 
-----------------Have fun!------------------
""")
    time.sleep(3)
    play_menu()

def play_menu():
    print("\nHello, " + name + """\nWelcome to Rock, Paper, Scissors game.
----Main Menu---
Press 1 for Information.
Press 2 for Game.
Press 3 for Quit.
""")
    menu_selection = input("please select your option: \n")
    try:
        menu_selection_number = int(menu_selection)
        print("you have selected: ", menu_selection_number)
    except ValueError:
        print(" Invalid selection")
        play_menu()

    if menu_selection_number == 1:
        play_information()
    elif menu_selection_number == 2:
        play_game()
    elif menu_selection_number == 3:
        play_quit()
    else:
        print("Invaild selection \n")
        main_menu()

def play_quit():

    sys.exit("""Thank you for Playing!
Hope u enjoed it 
Bye!""")

def play_game():
    import random

    user = None
    k = True
    while k == True:
        computer = random.choice(['rock', 'r', 'paper', 'p', 'scissor', 's'])

        print("Choose: r for rock | p for paper  | s for scissor ")
        user = input().lower()
        if user not in ('rock', 'r', 'paper', 'p', 'scissor', 's'):
            print('Invalid Input')
            user = None

        if user == computer:
            print('----Game Drawn!---')
            print('Want to play Again? Y/N')
            a = input()
            if a == 'N' or a == 'n':
                k = False
        else:
            if computer == 'rock' or computer == 'r':
                if user == 'paper' or user == 'p':
                    print('Computer have rock --- Great! You Won')
                elif user == 'scissor' or user == 's':
                    print('Computer have rock --- Ahmm! Computer Won')
            elif computer == 'paper' or computer == 'p':
                if user == 'scissor' or user == 's':
                    print('Computer have paper--- Great! You Won')
                elif user == 'rock' or user == 'r':
                    print('computer have paper--- Ahmm! Computer Won')
            elif computer == 'scissor' or computer == 's':
                if user == 'rock' or user == 'r':
                    print('Computer have scissor--- Great! You Won')
                elif user == 'paper' or user == 'p':
                    print('Computer have scissor--- Ahmm! Computer Won')
            print('Want to play Again? Y/N')
            a = input()
            if a == 'N' or a == 'n':
                k = False
            play_menu()
play_menu()