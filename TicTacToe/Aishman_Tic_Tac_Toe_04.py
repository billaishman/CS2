#Name: Bill Aishman
#Description: This code plays a Tic-Tac-Toe game
#Bugs: 
#Features:
#Log: 1.0
'''
The tic-tac-toe algorithm
1. Welcome! Play TTT?
2. 1 or 2 players (machine can also play itself) this is when player is set to = 0
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

#This fnction prints the tic-tac-toe board
def print_grid():
#This line draws the board and puts the letter that is in the box array in the place of the array separated by a |
    print( str(box[0][0]) + " | " + str(box[0][1]) + " | " + str(box[0][2]))
#This line draws the line across the grid
    print("---------")
#This line draws the board and puts the letter that is in the box array in the place of the array separated by a |
    print( str(box[1][0]) + " | " + str(box[1][1]) + " | " + str(box[1][2]))
#This line draws the line across the grid
    print("---------")
#This line draws the board and puts the letter that is in the box array in the place of the array separated by a |
    print( str(box[2][0]) + " | " + str(box[2][1]) + " | " + str(box[2][2]))

#Player enters move
def player_input(player):
#This starts the while statment that will loop until the user enters a valid response
    while True:
#This is a try to find out if what the user enered is in the correct format of number from 1-3 for a row and a column
        try:
#This fills in the variables row and column from what the player inputs
            row, col = map(int, input("Player " + player + " enter your move (row, col): ").split(","))
#This checks if the numbers are between 1-3
            if 1 <= row <= 3 and 1 <= col <= 3:
#If the number is between 1-3 then it returns the variables.
                return row, col
#If the input is not between 1-3, it prompts the user to enter a number between 1-3
            else:
                print("Please enter a row and column between 1 and 3.")
#If what the user enters is not a number, it prompts the user to enter a number
        except ValueError:
            print("Please enter two numbers separated by a comma.")

#Check to see if there is a row, column or cross that is all one type of x or o
def check_win():
#This checks to see if the first row has all x's or o's, if so it returns a true.
    if box[0][0] == box[0][1] == box[0][2]:
        return True
#This checks to see if the second row has all x's or o's, if so it returns a true.
    if box[1][0] == box[1][1] == box[1][2]:
        return True
#This checks to see if the third row has all x's or o's, if so it returns a true.
    if box[2][0] == box[2][1] == box[2][2]:
        return True
#This checks to see if the first column has all x's or o's, if so it returns a true.
    if box[0][0] == box[1][0] == box[2][0]:
        return True
#This checks to see if the second column has all x's or o's, if so it returns a true.
    if box[0][1] == box[1][1] == box[2][1]:
        return True
#This checks to see if the third column has all x's or o's, if so it returns a true.
    if box[0][2] == box[1][2] == box[2][2]:
        return True    
#This checks to see if a diagonal has all x's or o's, if so it returns a true.
    if box[0][0] == box[1][1] == box[2][2]:
        return True
#This checks to see if he other diagonal has all x's or o's, if so it returns a true.
    if box[0][2] == box[1][1] == box[2][0]:
        return True
#If none of them are true, it returns false
    return False
    
#ask player if they want x or o
def player_choice():
#This starts a while loop asking the user if x or o starts
    while True:
        X_O = input("X or O to start?")
        if X_O in ['X', 'O']:
#This returns the variables x and o if the user has entered an X or an O
            return X_O
#If the user does not enter an X or an O, the user is prompted to enter an X or and O
        else:
            print("Please type X or O.")

#Plays the tic-tac-toe game for two players
def game():
#This makes the variable for the player's choice of how many players
    player = player_choice()
#This sets the number of moves in a game to 9
    spaces = 9
#This starts the game that will play until nine moves have been made
    while True:
#This draws the grid
        print_grid()
#This runs the function to get the user input
        row, col = player_input(player)
#This checks to see if the spot is taken by checking the user input to the contents of the box array
        if box[row-1][col-1] == "X" or box[row-1][col-1] == "O":
#If the spot is taken, it prompts the user to enter another spot.
            print("Spot taken.")
        else:
#If the spot is not taken, it counts the move and removes one from the number of remaining moves
            spaces = spaces -1
#If the spot is not taken, it put the user's input into the spot.
            box[row-1][col-1] = player 
#This checks to see if the move was a winning move.
            if check_win():
#If the function check_win returns true, it prints the grid
                print_grid()
#If the function check_win returns true, it prints who won
                print("Player " + player + " wins!")
#If the function check_win returns true, the game quits
                quit()
#If the number of spaces gets to zero, the game quits as a tie
            if spaces == 0:
                print("Tie!")
                quit()
#After one round of moves, the play switches to the other player.
            if player == "O":
                player = "X"
            else:
                player = "O"           

#Plays the tic-tac-toe game for one player
def game_AI():
#This makes the variable for the player's choice of how many players
    player = player_choice()
#This sets the number of moves in a game to 9
    spaces = 9
#This starts the game that will play until nine moves have been made
    while True:
#This draws the grid
        print_grid()
#This runs the function to get the user input
        row, col = player_input(player)
#This checks to see if the spot is taken by checking the user input to the contents of the box array
        if box[row-1][col-1] == "X" or box[row-1][col-1] == "O":
#If the spot is taken, it prompts the user to enter another spot.
            print("Spot taken.")
        else:
#If the spot is not taken, it counts the move and removes one from the number of remaining moves
            spaces = spaces -1
#If the spot is not taken, it put the user's input into the spot.
            box[row-1][col-1] = player 
#This checks to see if the move was a winning move.
            if check_win():
#If the function check_win returns true, it prints the grid
                print_grid()
#If the function check_win returns true, it prints who won
                print("Player " + player + " wins!")
#If the function check_win returns true, the game quits
                quit()
#If the number of spaces gets to zero, the game quits as a tie
            if spaces == 0:
                print("Tie!")
                quit()
#After one round of moves, the play switches to the other player.
            if player == "O":
                player = "X"
            else:
                player = "O" 
#This starts a while loop that will run until an empty space is found
            while True:
                if box[row-1][col-1] == "X" or box[row-1][col-1] == "O":
#This find a random number for the row
                    row = random.randint(1,3)
#This find a random number for the column
                    col = random.randint(1,3)
                else:
                    break    
#This assigns the random number row and column to the bow array
            box[row-1][col-1] = player
#This counts the move and removes one space from the remaining number of moves
            spaces = spaces -1
#This checks to see if the move was a winning move.
            if check_win():
#If the function check_win returns true, it prints the grid
                print_grid()
#If the function check_win returns true, it prints who won
                print("Player " + player +" wins!")
#If the function check_win returns true, the game quits
                quit()
            if spaces == 0:
#If the number of spaces gets to zero, the game quits as a tie
                print("Tie!")
                quit()
#After one round of moves, the play switches to the other player.
            if player == "O":
                player = "X"
            else:
                player = "O"   

#This is where the computer plays itself
def game_alone():
#This sets the starting palyer as X
    player = "X"
#This sets the number of moves to 9
    spaces = 9
#This starts the while loop that will play until the number of moves is left is zero
    while True:
#This draws the grid
        print_grid()
#This starts a while loop that will run until an empty space is found
        while True:
#This find a random number for the row
            row = random.randint(1,3)
#This find a random number for the column
            col = random.randint(1,3)
#This finds if the spot is already taken
            if box[row-1][col-1] == "X" or box[row-1][col-1] == "O":
#If the spot is already taken, it finds a new random row and column
                row = random.randint(1,3)
                col = random.randint(1,3)
            else:
                break   
        if box[row-1][col-1] == "X" or box[row-1][col-1] == "O":
#IF the spot is taken it says the spot is taken
            print("Spot taken.")
#If the spot is not tkaen, it fill the spot in on the array
        else:
            box[row-1][col-1] = player
#This counts the move and removes one space from the remaining number of moves
            spaces = spaces - 1
#This checks to see if the move was a winning move.
            if check_win():
#If the function check_win returns true, it prints the grid
                print_grid()
#If the function check_win returns true, it prints who won
                print("Player " + player +  " wins!")
#If the function check_win returns true, the game quits
                quit()
#If the number of spaces gets to zero, the game quits as a tie
            if spaces == 0:
                print("Tie!")
                quit()
#After one round of moves, the play switches to the other player.
            if player == "O":
                player = "X"
            else:
                player = "O"
            
        
#Game opening
#This starts a while that will run as long as the game is running
while True:
#This asks if the user want to play.
    answer = input("Welcome! Play TTT? (y or n)")
#If the user wants to play, it asks how many players
    if answer == str.lower("y"):  
#This starts a while loop that will run until the user answers how many players   
            while True:
#This asks the user how many players
                player_count = input("0, 1 or 2 players?")
#If the user says 0 players, it runs the game_alone function
                if player_count == str.lower("0"):
                    game_alone()
                    print("Thanks for playing!")
                    quit()
#If the user says 1 player, it runs the game_AI function
                if player_count == str.lower("1"):
                    game_AI()
                    print("Thanks for playing!")
                    quit()
#If the user says 2 player, it runs the game function
                if player_count == str.lower("2"):
                    game()
                    print("Thanks for playing!")
                    quit()
#IF the user does not enter a 0,1,2, it prompts the user
                else:
                    print("Please enter 0, 1 or 2.")
#If the user does not want to play, it ends the game
    if answer == str.lower("n"):
        print("Bye!")
        break 
#if the user does not enter a y or n, it prompts the user.
    else:
        print("Please enter y or n")
