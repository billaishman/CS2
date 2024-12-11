#Name: Bill Aishman
#Description: This code plays a Hangman game
#Bugs: 
#Features:
#Log: 1.0
'''
The hangman algorithm
1. Design the word selection and storage mechanism
2. Create the basic game loop
3. Implement input validation
4. Add the hangman display
5. Develop win/lose conditions
6. Implement optional advanced features
7. Thoroughly test the game
8. Write documentation
'''

#Imports the random library for the computer player
import random

#This draws the hangman
Hangman = ['''
  -----
  |   |
  |
  |
  |
  |
***********''', '''
  -----
  |   |
  |   O
  |
  |
  |
***********''', '''
  -----
  |   |
  |   O
  |   |
  |
  |
***********''', '''
  -----
  |   |
  |   O
  |   |-
  |
  |
***********''', '''
  -----
  |   |
  |   O
  |  -|-
  |
  |
***********''', '''
  -----
  |   |
  |   O
  |  -|-
  |  |
  |
***********''', '''
  -----
  |   |
  |   O
  |  -|-
  |  | |
  |
***********''']

#This is the word list
word_list = ["bill", "class", "computer"]
#This chooses the word
the_word=random.choice(word_list)
chosen_word = list(the_word)
#This makes the number of blanks to display
blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)

#This variable is which hangman to show
man = 0

#This is the user input
def guessing():
    x = 0
    global man
    correct_guess = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            print("Correct! There is a '" + guess + "' !")
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
        
    if correct_guess == False:
        print("Sorry, there is no '" + guess + "'.")
        man += 1
    x = 0

while man < 6:
    if blank_list == chosen_word:
        print("Correct! The answer was: '" + the_word + "'")
        break
    print(Hangman[man])
    print("This is the word you are guessing: " + ''.join(blank_list))
    guess = input("Guess another letter:")
    guessing()

if man == 6:
    print("Nice try! The answer was: '" + the_word + "'")