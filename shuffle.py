''' Shuffle cups game'''
# TODO
# - add loop on win

from random import shuffle

# Greet function, uses the output from whoru()
def greet(name):
    reply = ''
    while reply not in ['Y','N','y','n']:
        reply = input(f"Hi {name.upper()}, do you want to play a game (Y/N)?: ")
        if reply in ['Y','y']:
            print(f"\nLet's play {name.upper()}!!!\n")
        else:
            print(f"\nSorry to see you leave, {name.upper()}. Bye!\n")
            exit()
    return (reply)

# Authentication function
def whoru():
    player = input("Hi stranger, how shall I refer to you?: ")
    while not player:
        player = input("Hi stranger, how shall I refer to you?: ")
    return (player)

# Function to shuffle a list
def shuffled(my_list):
    shuffle(my_list)
    return my_list

# Function to handle player's guess
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("What's the ball? 0, 1 or 2?: ")
    return int(guess)

# Function to check player's guess
def check_guess(shuffled_cups,player_guess):
    if shuffled_cups[player_guess] == 'O':
        print(f"\nYes you guessed it! YOU WIN, {player.upper()}!!!")
    else:
        print(f"\nYou guessed wrong. It was in: {shuffled_cups}\n")

# PLayer authentication
player = whoru()

# Greeting
greet(player)

# 1. Setup list
cups = ['', 'O', '']

# 2. Shuffle cups
mixed_cups = shuffled(cups)

# 3. Get user's guess index
guess = player_guess()

# 4. Check if player guess matches0
check_guess(mixed_cups, guess)