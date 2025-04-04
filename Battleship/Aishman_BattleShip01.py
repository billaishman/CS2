'''
┌───────────────────────────────────────────────────────────────────────────┐
│                           Battleship                           │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Bill Aishman                                                        │
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description: This code makes a playable battleship game either aginst     |
| a player or a computer                                                    |                             
└───────────────────────────────────────────────────────────────────────────┘
'''
#Imports the random library for the computer player
import random


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

def place_ship():
    count = 0
    #This is how many ships are placed
    while count < 4:
        row = random.randint(1,5)
        col = random.randint(1,5)
        if box2[row-1][col-1] == "🚢":
            row = random.randint(1,5)
            col = random.randint(1,5)
        else:
            box2[row-1][col-1] = "🚢"
        count += 1

#Player enters move
def player_input():
    while True:
        try:
            row, col = map(int, input("Enter your move (row, col): ").split(","))
            if 1 <= row <= 5 and 1 <= col <= 5:
                return row, col
            else:
                print("Please enter a row and column between 1 and 3.")
        except ValueError:
            print("Please enter two numbers separated by a comma.")

def game():
        place_ship()
        count = 10
        hits = 0
        while count != 0:
            print_grid()
            print("You have " + str(count) + " moves left.")
            row, col = player_input()
            count = count - 1
            if box2[row-1][col-1] == "🚢":
                box[row-1][col-1] = "🔥"
                box2[row-1][col-1] = "🔥"
                print("You Hit One!")
                hits += 1
                if hits == 4:
                    print_grid2()
                    print("You Win!")
                    exit()
            else:
                box[row-1][col-1] = "M"
                box2[row-1][col-1] = "M"
                print("You Missed!")
        print_grid2()
        print("Here they were!")
        print("Game Over!")

def main():
    game()

main()