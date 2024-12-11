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
 
def making_a_guess():
    x = 0
    global update_display
    correct_guess = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
    if correct_guess == False:
        print(f"There is no {guess}, sorry.")
        update_display += 1
    x = 0
 
 
Hangman = ['''
  +---+
  |   |
  |
  |
  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |
  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |   |
  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |   |-
  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |  -|-
  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |  -|-
  |  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |  -|-
  |  | |
  |
=========''']
 
word_list = ["bill", "class", "computer"]
chosen_word = list(random.choice(word_list))


blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)
 
update_display = 0
 
#----------------------------------------------------------------------------------------------
 
print(Hangman[update_display])
guess = input(f"Welcome to hangman.\n{blank}\nGuess your letter: ")
making_a_guess()
print(Hangman[update_display])
print(''.join(blank_list))

while update_display < 6:
    if blank_list == chosen_word:
        print("Correct!")
        break
    guess = input("Make another guess? ")
    making_a_guess()
    print(Hangman[update_display])
    print(''.join(blank_list))
if update_display == 6:
    print("Nice try! The answer was:")
    print(chosen_word)