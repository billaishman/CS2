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

#This imports the random library for the computer player
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

#This variable is which hangman to show and counts how many chances
man = 0

#This is the user input
def guessing():
    x = 0
    global man
    correct_guess = False
    #This for loop checks if the guess letter is in the chosen word
    for letter in chosen_word:
        #if the guess in the word it says correct and then adds that letter to the blanks
        if guess.lower() == chosen_word[x]:
            print("Correct! There is a '" + guess + "' !")
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
    #if the guess is incorrect then it goes to the next man    
    if correct_guess == False:
        print("Sorry, there is no '" + guess + "'.")
        man += 1
    x = 0

#This is the main while loop counts the number of guesses up to 6
while man < 6:
    if blank_list == chosen_word:
        print("Correct! The answer was: '" + the_word + "'")
        break
    print(Hangman[man])
    print("This is the word you are guessing: " + ''.join(blank_list))
    guess = input("Guess another letter:")
    guessing()
#If you make 6 guesses, you are done
if man == 6:
    print(Hangman[man])
    print("Nice try! The answer was: '" + the_word + "'")