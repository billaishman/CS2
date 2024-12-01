#Name: Bill Aishman
#Description: This code plays a Tic-Tac-Toe game
#Bugs: 
#Features:
#Log: 1.0
'''
The tic-tac-toe algorithm
1. Welcome! Play TTT?
2. 1 or 2 players (machine can also play itself) this is when player = 0
3. Determine X or O
4. Draw the Board/Label coords
5. Loop 9 or break
6. Ask the player where they want go
7. If exists prior turn -- then 'spot taken' /else place choice
8. Check win?
8a. Display the Board
9. Player 2 (user or machine)
10 .....if machine --random --- if spot it chose -- choose another random
'''

#Imports the random library for the computer player
import random

#This is initializes the array that will hold the tic-tac-toe places
box = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#Prints the tic-tac-toe board
def print_grid():
    print( str(box[0][0]) + " | " + str(box[0][1]) + " | " + str(box[0][2]))
    print("---------")
    print( str(box[1][0]) + " | " + str(box[1][1]) + " | " + str(box[1][2]))
    print("---------")
    print( str(box[2][0]) + " | " + str(box[2][1]) + " | " + str(box[2][2]))

#Player enters move
def player_input(player):
    while True:
        try:
            row, col = map(int, input("Player " + player + " enter your move (row, col): ").split(","))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row, col
            else:
                print("Please enter a row and column between 1 and 3.")
        except ValueError:
            print("Please enter two numbers separated by a comma.")

#Check to see if there is a row, column or cross that is all one type of x or o
def check_win():
    if box[0][0] == box[0][1] == box[0][2]:
        return True
    if box[1][0] == box[1][1] == box[1][2]:
        return True
    if box[2][0] == box[2][1] == box[2][2]:
        return True
    if box[0][0] == box[1][0] == box[2][0]:
        return True
    if box[0][1] == box[1][1] == box[2][1]:
        return True
    if box[0][2] == box[1][2] == box[2][2]:
        return True    
    if box[0][0] == box[1][1] == box[2][2]:
        return True
    if box[0][2] == box[1][1] == box[2][0]:
        return True
    return False
    
#ask player if they want x or o
def player_choice():
    while True:
        X_O = input("X or O to start?")
        if X_O in ['X', 'O']:
            return X_O
        else:
            print("Please type X or O.")

#Plays the tic-tac-toe game for two players
def game():
    player = player_choice()
    spaces = 9
    while True:
        print_grid()
        row, col = player_input(player)
        if box[row-1][col-1] == "X" or box[row-1][col-1] == "O":
            print("Spot taken.")
        else:
            spaces = spaces -1
            box[row-1][col-1] = player 
            if check_win():
                print_grid()
                print("Player " + player + " wins!")
                quit()
            if spaces == 0:
                print("Tie!")
                quit()
            if player == "O":
                player = "X"
            else:
                player = "O"           

#Plays the tic-tac-toe game for one player
def game_AI():
    player = player_choice()
    spaces = 9
    while True:
        print_grid()
        row, col = player_input(player)
        if box[row-1][col-1] == "X" or box[row-1][col-1] == "O":
            print("Spot taken.")
        else:
            box[row-1][col-1] = player
            spaces = spaces - 1
            if check_win():
                print_grid()
                print("Player " + player +  " wins!")
                quit()
            if spaces == 0:
                print("Tie!")
                quit()
            if player == "O":
                player = "X"
            else:
                player = "O"
            while True:
                if box[row-1][col-1] == "X" or box[row-1][col-1] == "O":
                    row = random.randint(1,3)
                    col = random.randint(1,3)
                else:
                    break    
            box[row-1][col-1] = player
            spaces = spaces -1
            if check_win():
                print_grid()
                print("Player " + player +" wins!")
                quit()
            if spaces == 0:
                print("Tie!")
                quit()
            if player == "O":
                player = "X"
            else:
                player = "O"
                    
#Game opening
while True:
    answer = input("Welcome! Play TTT? (y or n)")
    if answer == str.lower("y"):     
            while True:
                player_count = input("1 or 2 players?")
                if player_count == str.lower("1"):
                    game_AI()
                    print("Thanks for playing!")
                    quit()
                if player_count == str.lower("2"):
                    game()
                    print("Thanks for playing!")
                    quit()
                else:
                    print("Please enter 1 or 2.")
    if answer == str.lower("n"):
        print("Bye!")
        break 
    else:
        print("Please enter y or n")
