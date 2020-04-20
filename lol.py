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
            elif user == 'scissor'or user == 's':
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



