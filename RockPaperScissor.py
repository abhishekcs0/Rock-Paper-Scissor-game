from random import randint
import emoji

def game(player):

    move = ["rock", "paper", "scissor"]
    emojis = {"rock":emoji.emojize(":raised_fist:"),"paper": emoji.emojize(":raised_hand:"),"scissor": emoji.emojize(":victory_hand:") }
    computer = move[randint(0, 2)]

    if computer == "rock" and player == "paper":
        print(f"player : {emojis[player]} computer : {emojis[computer]} \nyou win!")

    elif computer == "rock" and player == "scissor":
        print(f"player : {emojis[player]} computer : {emojis[computer]} \nyou lose!")

    elif computer == "paper" and player == "scissor":
        print(f"player : {emojis[player]} computer : {emojis[computer]} \nyou win!")

    elif computer == "paper" and player == "rock":
        print(f"player : {emojis[player]} computer : {emojis[computer]} \nyou lose")

    elif computer == "scissor" and player == "rock":
        print(f"player : {emojis[player]} computer : {emojis[computer]} \nyou win!")

    elif computer == "scissor" and player == "paper":
        print(f"player : {emojis[player]} computer : {emojis[computer]} \nyou lose!")

    else:
        print(f"player : {emojis[player]} computer : {emojis[computer]} \nTie")

def player_move():
    pmove = input("'rock' 'paper' 'scissor'? ")

    while pmove not in ['rock','paper' , 'scissor']:
        print("Wrong Input! Choose Again")

        pmove = input("'rock' 'paper' 'scissor'? ")

    return pmove

#gameon
gameon = True

while gameon:
    player = input()

    game(player_move())

    exit = input("if you wanna continue type: 'yes' else type:'exit'")

    while exit != "yes" and  exit != "exit":
        print("ohh wrong input please give correct input!")
        exit = input("if you wanna continue type: 'yes' else type:'exit'")

    if exit == "exit":
        print("Thanks for playing!")
        gameon = False
