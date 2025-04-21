'''
┌───────────────────────────────────────────────────────────────────────────┐
│                           Battleship                                      │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Bill Aishman                                                        │
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description: This code makes a playable battleship game against a computer|
|                                                                           |                             
└───────────────────────────────────────────────────────────────────────────┘
'''
#Imports the random library for the computer player
import random
#imports the audio for the game
import pygame
pygame.mixer.init()  # Initialize the mixer module.
sound1 = pygame.mixer.Sound(r"Bomb_sound.wav")  # Load a sound.

#This is initializes the array that the player will see
box = [
    ['X','X','X','X','X'],
    ['X','X','X','X','X'],
    ['X','X','X','X','X'],
    ['X','X','X','X','X'],
    ['X','X','X','X','X'],
]

#This is initializes the array that will hold the ships
box2 = [
    ['X','X','X','X','X'],
    ['X','X','X','X','X'],
    ['X','X','X','X','X'],
    ['X','X','X','X','X'],
    ['X','X','X','X','X'],
]
#Prints the board with the hidden ships
def print_grid2():
    print( "   | " + "1" + "  | " + "2" + "  | " + "3" + "  | " + "4" + "  | " + "5" + " | ")
    print("----------------------------")
    print( "1  | " + str(box2[0][0]) + "  | " + str(box2[0][1]) + "  | " + str(box2[0][2])+ "  | " + str(box2[0][3]) + "  | " + str(box2[0][4])+ " | ")
    print("----------------------------")
    print( "2  | " + str(box2[1][0]) + "  | " + str(box2[1][1]) + "  | " + str(box2[1][2])+ "  | " + str(box2[1][3]) + "  | " + str(box2[1][4])+ " | ")
    print("----------------------------")
    print( "3  | " + str(box2[2][0]) + "  | " + str(box2[2][1]) + "  | " + str(box2[2][2])+ "  | " + str(box2[2][3]) + "  | " + str(box2[2][4])+ " | ")
    print("----------------------------")
    print( "4  | " + str(box2[3][0]) + "  | " + str(box2[3][1]) + "  | " + str(box2[3][2])+ "  | " + str(box2[3][3]) + "  | " + str(box2[3][4])+ " | ")
    print("----------------------------")
    print( "5  | " + str(box2[4][0]) + "  | " + str(box2[4][1]) + "  | " + str(box2[4][2])+ "  | " + str(box2[4][3]) + "  | " + str(box2[4][4])+ " | ")
    print("----------------------------")


#Prints the board the player sees
def print_grid():
    print( "   | " + "1" + "  | " + "2" + "  | " + "3" + "  | " + "4" + "  | " + "5" + " | ")
    print("----------------------------")
    print( "1  | " + str(box[0][0]) + "  | " + str(box[0][1]) + "  | " + str(box[0][2])+ "  | " + str(box[0][3]) + "  | " + str(box[0][4])+ " | ")
    print("----------------------------")
    print( "2  | " + str(box[1][0]) + "  | " + str(box[1][1]) + "  | " + str(box[1][2])+ "  | " + str(box[1][3]) + "  | " + str(box[1][4])+ " | ")
    print("----------------------------")
    print( "3  | " + str(box[2][0]) + "  | " + str(box[2][1]) + "  | " + str(box[2][2])+ "  | " + str(box[2][3]) + "  | " + str(box[2][4])+ " | ")
    print("----------------------------")
    print( "4  | " + str(box[3][0]) + "  | " + str(box[3][1]) + "  | " + str(box[3][2])+ "  | " + str(box[3][3]) + "  | " + str(box[3][4])+ " | ")
    print("----------------------------")
    print( "5  | " + str(box[4][0]) + "  | " + str(box[4][1]) + "  | " + str(box[4][2])+ "  | " + str(box[4][3]) + "  | " + str(box[4][4])+ " | ")
    print("----------------------------")

#This randomly places the ships in the array that holds the ships
def place_ship():
    count = 0 #This sets the ship count to zero
    #This is how many ships are placed
    while count < 4:
        row = random.randint(1,5) #This chooses a random number between 1 and 5 for the row number
        col = random.randint(1,5) #This chooses a random number between 1 and 5 for the column number
        if box2[row-1][col-1] == "🚢": #If the random row and column already has a ship, it chooses another random spot
            row = random.randint(1,5)#This chooses a random number between 1 and 5 for the row number
            col = random.randint(1,5)#This chooses a random number between 1 and 5 for the column number
        else:
            box2[row-1][col-1] = "🚢" #If the random row and column is empty, it puts a ship there
        count += 1 #This adds one to the ship count

#Player enters move
def player_input():
    while True: #This runs the loop and makes sure the user enters numbers correctly
        try:
            row, col = map(int, input("Enter your move (row, col): ").split(","))#This asks the user the row and column and then assigns each variable
            if 1 <= row <= 5 and 1 <= col <= 5:#This makes sure the user number is between 1 and 5
                return row, col #This returns the row and column
            else:
                print("Please enter a row and column between 1 and 3.") #This prompts the user to enter properly
        except ValueError:
            print("Please enter two numbers separated by a comma.") #This prompts the user to enter properly

#This is the main body of the game
def game():
        place_ship() #This runs place ship to place the ships
        count = 10 #This is the number of moves the player gets
        hits = 0 #This sets the number of hits to zero
        while count != 0: #This runs the loop while the player still has moves
            print_grid() #This prints what the use sees
            print("You have " + str(count) + " moves left.") #This tells the user how many moves they have
            row, col = player_input() #This takes the row and column the user enters.
            count = count - 1 #This removes one of the user's moves.
            if box2[row-1][col-1] == "🚢": #If the user has picked a spot with a ship
                box[row-1][col-1] = "🔥" #It makes a fire on what the user sees.
                box2[row-1][col-1] = "🔥" #It makes a fire on the bos the user does not see.
                sound1.play() #This plays the sound of the bomb.
                print("You Hit One!") #This tells the user they got a hit.
                hits += 1 #This increases the hits by 1
                if hits == 4: #This checks to see if the user has hit 4 ships
                    print_grid2() #This prints the grid where the ship were
                    print("You Win!") #This tells the user they won
                    exit() #This ends the game
            else: #If the spot does not have a ship in it
                box[row-1][col-1] = "M" #It makes a M on what the user sees.
                box2[row-1][col-1] = "M" #It makes a M on what the user does not see.
                print("You Missed!") #This tells the user they missed.
        print_grid2() #This prints the game board and shows the user where the ships were.
        print("Here they were!") #This tells the user where they were.
        print("Game Over!") #This tells the user the game is over.

#This runs the main
def main(): 
    game() #This runs game

main() #This runs main
