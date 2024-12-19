#-------------------------------------------------------------------------------#
# Name: Bill Aishman                                                            #
# Log: Finished project (1.0)                                                   #
# Description: This is a hangman game. It selects a random word from dictionary.#
# The user then guesses letters. If the user guesses all of the letters, the    #
# user wins! The user can get six letters wrong and then the game is over.      # 
#-------------------------------------------------------------------------------#

#This imports the random library for the computer player.
import random

#This draws six versions of the hangman.
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
#This is where it reads in the word list by opening the file in read mode.
#The file name can be changed to whatever dictionary you want.
#This dictionary happens to be all the words allowed in wordle.
my_file = open("official_allowed_guesses.txt", "r") 
  
#This puts the text from the file into a variable 
data = my_file.read() 
  
#This parses the data when newline ('\n') is seen. 
word_list = data.split("\n") 

#This randomly chooses a word from parsed data.
the_word = random.choice(word_list)

#This turns the randomly chosen word into a list of letters.
chosen_word = list(the_word)

#This makes the number of blanks to display
blank = ""

#This makes a list of blank spaces the same length as the list of letters in the word.
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)

#This variable is which hangman to show and counts how many chances the user has left
man = 0

#This is the list of previous guesses
wrong_guess = []

#This is a function that checks if the user input is correct.
def guessing():
    #This sets some of the variables
    x = 0
    global man
    #This sets the correct guess to false.
    correct_guess = False
    #This for loop checks if the guess letter is in the chosen word.
    for letter in chosen_word:
        #if the guess in the word it says correct and then adds that letter to the blanks.
        if guess.lower() == chosen_word[x]:
            #This prints if the user was correct.
            print("Correct! There is a '" + guess + "' !")
            #This updates the list of blanks with the correct letter.
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
    #if the guess is incorrect then it displays the next hangman    
    if correct_guess == False:
        #This adds to the list of incorrect guesses for the user.
        wrong_guess.append(guess)
        print("Sorry, there is no '" + guess + "'.")
        man += 1
    x = 0

#This is the main while loop counts the number of guesses up to 6
while man < 6:
    if blank_list == chosen_word:
        print("Correct! The answer was: '" + the_word + "'")
        break
    print(Hangman[man])
    print("These are the wrong guesses so far:", wrong_guess)
    print("You have", 6-man ,"guesses left.")
    print("This is the word you are guessing: " + ''.join(blank_list))
    guess = input("Guess another letter:")
    guessing()
#If you make 6 guesses, you are done
if man == 6:
    print(Hangman[man])
    print("Nice try! The answer was: '" + the_word + "'")