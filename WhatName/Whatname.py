#-------------------------------------------------------------------------------#
# Name: Bill Aishman                                                            
# Log: Finished project (1.0)                                                   
# Description: This is a string class of functions. Esch funtion manipulates a string
# List of Functions:
#   1. Reverse and display
#   2. Determine the number of vowels. You can prompt user for a particular vowel or create subtotals of each.
#   3. Consonant frequency. Bonus: Subtotals of each consonant
#   4. Return first name.
#   5. Return last name.
#   6. Return middle name(s)
#   7. Return boolean if last name contains a hyphen
#   8. Function to convert to lowercase
#   9. Function to convert to uppercase
#   10. Modify array to create a random name (mix up letters)
#   11. Return boolean if first name is a palindrome
#   12. Return full-name as a sorted array of characters (Bonus)
#   13. Build a menu (Bonus)
#   14. Make initials from name
#   15. Return boolean if name contains a title/distinction (“Dr.”, “Sir”, “Esq”, “Ph.d”)
#   (Bonus) 17. COME UP WITH YOUR OWN! (Bonus)
#   18. Secret Bonus ---See me
# 
#-------------------------------------------------------------------------------#

#This imports the random library for the random name function
import random

#   1. This function will reverse and display a user input
def reverse(x):
#This takes the list that the user inputs and then makes a new list with the reverse order
  reverse_name = x[::-1]
#This returns the new list
  return reverse_name

#   2. This function will determine the number of vowels and then create subtotals of each.
def vowels(x):
#This sets the variables for each of the vowels at zero to count them
  a_count = e_count = i_count = o_count = u_count = vowel_count = 0
#This starts a for loop for each of the characters in the user name
  for char in x:
#This checks to see if it is that right character
    if char == 'a' or char == 'A':
#This increases the counter by one if it is the right letter
      a_count += 1
#This increases the vowel counter by one if it is a vowel
      vowel_count +=1
#This checks to see if it is that right character
    if char == 'e' or char == 'E':
#This increases the counter by one if it is the right letter
      e_count += 1
#This increases the vowel counter by one if it is a vowel
      vowel_count +=1
#This checks to see if it is that right character
    if char == 'i' or char == 'I':
#This increases the counter by one if it is the right letter
      i_count += 1
#This increases the vowel counter by one if it is a vowel
      vowel_count +=1
#This checks to see if it is that right character
    if char == 'o' or char == 'O':
#This increases the counter by one if it is the right letter
      o_count += 1
#This increases the vowel counter by one if it is a vowel
      vowel_count +=1
#This checks to see if it is that right character
    if char == 'u' or char == 'U':
#This increases the counter by one if it is the right letter
      u_count += 1
#This increases the vowel counter by one if it is a vowel
      vowel_count +=1
#This returns each of the vowels and the total
  return("2. There are " + str(a_count) + " a's in your name. \n2. There are " 
        + str(e_count) + " e's in your name. \n2. There are " 
        + str(i_count) + " i's in your name. \n2. There are " 
        + str(o_count) + " o's in your name. \n2. There are " 
        + str(u_count) 
        + " u's in your name. \n2. There are " + str(vowel_count) + " total vowels in your name.")

#   3. Consonant frequency. Bonus: Subtotals of each consonant
def consonant(x):
#This sets the variables for each of the consonants at zero to count them
  b_count = c_count = d_count = f_count = g_count = h_count = j_count = k_count = l_count = m_count = n_count = p_count = q_count = r_count = s_count = t_count = u_count = v_count = w_count = x_count = y_count = z_count = consonant_count = 0
#This starts a for loop for each of the characters in the user name
  for char in x:
#This checks to see if it is that right character
    if char == 'b' or char == 'B':
#This increases the counter by one if it is the right letter
      b_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'c' or char == 'C':
#This increases the counter by one if it is the right letter
      c_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'd' or char == 'D':
#This increases the counter by one if it is the right letter
      d_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'f' or char == 'F':
#This increases the counter by one if it is the right letter
      f_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'g' or char == 'G':
#This increases the counter by one if it is the right letter
      g_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'h' or char == 'H':
#This increases the counter by one if it is the right letter
      h_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'j' or char == 'J':
#This increases the counter by one if it is the right letter
      j_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'k' or char == 'K':
#This increases the counter by one if it is the right letter
      k_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'l' or char == 'L':
#This increases the counter by one if it is the right letter
      l_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'm' or char == 'M':
#This increases the counter by one if it is the right letter
      m_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'n' or char == 'N':
#This increases the counter by one if it is the right letter
      n_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'p' or char == 'P':
#This increases the counter by one if it is the right letter
      p_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'q' or char == 'Q':
#This increases the counter by one if it is the right letter
      q_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'r' or char == 'R':
#This increases the counter by one if it is the right letter
      r_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 's' or char == 'S':
#This increases the counter by one if it is the right letter
      s_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 't' or char == 'T':
#This increases the counter by one if it is the right letter
      t_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'v' or char == 'V':
#This increases the counter by one if it is the right letter
      v_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'w' or char == 'W':
#This increases the counter by one if it is the right letter
      w_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'x' or char == 'X':
#This increases the counter by one if it is the right letter
      x_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'y' or char == 'Y':
#This increases the counter by one if it is the right letter
      y_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This checks to see if it is that right character
    if char == 'z' or char == 'Z':
#This increases the counter by one if it is the right letter
      z_count += 1
#This increases the consonant counter by one if it is a consonant
      consonant_count +=1
#This returns each of the consonants and the total
  return("3. There are " + str(b_count) + " b's in your name. \n3. There are " + 
        str(c_count) + " c's in your name. \n There are " + 
        str(d_count) + " d's in your name. \n There are " +
        str(f_count) + " f's in your name. \n There are " + 
        str(g_count) + " g's in your name. \n There are " + 
        str(h_count) + " h's in your name. \n There are " + 
        str(j_count) + " j's in your name. \n There are " +
        str(k_count) + " k's in your name. \n There are " + 
        str(l_count) + " l's in your name. \n There are " + 
        str(m_count) + " m's in your name. \n There are " + 
        str(n_count) + " n's in your name. \n There are " +
        str(p_count) + " p's in your name. \n There are " + 
        str(q_count) + " q's in your name. \n There are " + 
        str(r_count) + " r's in your name. \n There are " + 
        str(s_count) + " s's in your name. \n There are " +
        str(t_count) + " t's in your name. \n There are " + 
        str(v_count) + " v's in your name. \n There are " +
        str(w_count) + " w's in your name. \n There are " + 
        str(x_count) + " x's in your name. \n There are " +
        str(y_count) + " y's in your name. \n There are " + 
        str(z_count) + " z's in your name. \n There are " + 
        str(consonant_count) + " total consonants in your name.")

#   4. This function will print the first name entered.
def firstname(x):
#This makes an empty list to fill
  name_split = []
#This starts a variable that is empty
  word = ""  
#This starts a loop for all of the characters in the user's name
  for char in x: 
#This checks to see if the character is not a space 
    if char != " ": 
#If is is not a space, it adds the charater to the variable word
        word += char  
#If the character is a space, it adds the current word to the name_split list
    else:  
        name_split.append(word) 
#This then resests the current word to nothing
        word = ""  
#This the puts the last word into the name_split list
  if word:  
      name_split.append(word)
#This runs the check first function to see if there is something in front of the first name
  if checkfirst(x) == True:
#If there is something in front of the firts word, then it sets a varibale equal to the second word
    fn = name_split[1]
#If there is nothing in front of the firts word, then it sets a varibale equal to the first word
  elif checkfirst(x) == False:
    fn = name_split[0]
#This returns the first name
  return((fn))

#   5. Return last name.
def lastname(x):
#This makes an empty list to fill
  name_split = [] 
#This starts a variable that is empty
  word = "" 
#This starts a loop for all of the characters in the user's name
  for char in x:  
#This checks to see if the character is not a space 
    if char != " ": 
#If is is not a space, it adds the charater to the variable word
        word += char
#If the character is a space, it adds the current word to the name_split list  
    else:  
        name_split.append(word) 
#This then resests the current word to nothing
        word = ""  
#This the puts the last word into the name_split list
  if word:  
      name_split.append(word)
#This returns the last word in the list
  return(name_split[-1])

#   6. Return middle name(s)
def middlename(x):
#This makes an empty list to fill
  name_split = [] 
#This starts a variable that is empty
  word = ""  
#This starts a loop for all of the characters in the user's name
  for char in x:  
#This checks to see if the character is not a space
    if char != " ": 
#If is is not a space, it adds the charater to the variable word
        word += char 
#If the character is a space, it adds the current word to the name_split list 
    else:  
        name_split.append(word) 
#This then resests the current word to nothing
        word = ""  
#This the puts the last word into the name_split list
  if word:  
      name_split.append(word)
#This runs the check first function to see if there is something in front of the first name
  if checkfirst(x) == True:
#If there is something in front of the first word, then it make a new list with everything past the second word
    fn = name_split[2:]
#This removes the last word of the list
    fn = fn[:-1]
#If there is nothing in front of the first word, then it make a new list with everything past the first word
  elif checkfirst(x) == False:
    fn = name_split[1:]
#This removes the last word of the list
    fn = fn[:-1]
#This returns the middle words
  return(str(fn))

#   7. Return boolean if last name contains a hyphen
def hyphen(x):
#This checks to see if there is a - in the word
  if '-' in x:
#If there is, it returns true
    return True
#If there is not, it returns false
  else:
    return False

#   8. Function to convert to lowercase
def lower(x):
#This starts an empty variable
  lower_case = ""
#This starts a for loop for every character in the person's name
  for char in x:
#This checks if the character is upper case
      if 'A' <= char <= 'Z':
#If it is uppercase, it adds the letter 32 more than it (the lowercase letter)
          lower_case += chr(ord(char) + 32)
      else:
#If not, it just adds the letter
          lower_case += char
#This returns the variable
  return (lower_case)

#   9. Function to convert to uppercase
def upper(x):
#This starts an empty variable
  upper_case = ""
#This starts a for loop for every character in the person's name
  for char in x:
#This checks if the character is lower case
      if 'a' <= char <= 'z':
#If it is lowercase, it adds the latter 32 less than it (the uppercase letter)
          upper_case += chr(ord(char) - 32)
      else:
#If not, it just adds the letter
          upper_case += char
#This returns the variable
  return (upper_case)

#   10. Modify array to create a random name (mix up letters)
def random_name(x):
#This makes an empty list to fill
  word = []
#This starts a for loop for every character in the person's name
  for char in x:
#This puts every letter in the variable
    word.append(char)
#This shuffles the letters
  random.shuffle(word)
#This rejoins and then returns the variable
  return(''.join(word))

#   11. Return boolean if first name is a palindrome
def palindrome(x):
#This makes an empty list to fill
  name_split = [] 
#This starts an empty variable
  word = "" 
#This starts a for loop for every character in the person's name 
  for char in x:  
#This checks to see if the character is not a space
    if char != " ": 
#If it is not a space, it adds it to the word
        word += char  
#If is a space, it adds the current word to the list
    else:  
        name_split.append(word) 
#This resests the word to nothing
        word = ""  
#This adds the last word to the list
  if word:  
      name_split.append(word)
#This checks to see if there is a word in front of the first name
  if checkfirst(x) == True:
#If there is a word in front of the first, it starts the palindrome list from the second word
    palindrome_first = name_split[1]
#This reverses and returns the first word
    return palindrome_first == palindrome_first[::-1]
#If there is not a word in front of the first, it starts the palindrome list from the first word
  elif checkfirst(x) == False:
    palindrome_first = name_split[0]
#This reverses and returns the first word
    return palindrome_first == palindrome_first[::-1]
  
#   12. Return full-name as a sorted array of characters (Bonus)
def name_sort(x):
#This makes an empty list to fill
  word = []
#This starts a for loop for every character in the person's name 
  for char in x:
#This fills the variabe word with the letters from the person's name
    word.append(char)
#This runs a loop for the length of the word
  for i in range(0, len(word)):
#This runs a loop for each of the next letters of the word
    for j in range(i+1, len(word)):
#This checks to see if the letter is bigger than the next letter
        if word[i] >= word[j]:
#IF is is, it reverses the letters
           word[i], word[j] = word[j],word[i]
  print("12. Your name's letters sorted: ")
#This returns the ordered letters
  return(word)

#   13. Build a menu (Bonus)
#   14. Make initials from name
def initials(x):
#This makes an empty list to fill
  name_split = []
#This starts an empty variable
  initials = ""
#This starts an empty variable
  word = ""
#This starts a for loop for every character in the person's name 
  for char in x:  
#This checks to see if the character is not a space
    if char != " ": 
#If it is not a space, it add the char to the word
        word += char  
    else:  
#If is is a space, it adds the word to the list
        name_split.append(word) 
#This resets the word to nothing
        word = "" 
#This adds the last word
    if word:  
      name_split.append(word)
#This starts a loop for all of the words in the list
  for initial in name_split:
#This takes the first letter of each word
    if initial == initial [0]:
#This adds the first letter of each word to the variable intitial
      initials += initial[0]
#This returns the variable initital
  return("14. Your initials are: " + initials)

#   15. Return boolean if name contains a title/distinction (“Dr.”, “Sir”, “Esq”, “Ph.d”)
def checkfirst(x):
#This is the list of titles
  stuff = ['Dr.', 'Doctor', 'Mr.', 'Ms.', 'Mrs.', 'Mister', 'Miss', 'Missus']
#This splits the user name if there is a space
  fn = x.split(" ")
#This checks to see if the first word is in the list
  if fn[0] in stuff: 
#If it is, it returns true
    return True
#If not, it returns false
  else:
    return False
  
#   (Bonus) 17. COME UP WITH YOUR OWN! (Bonus)
#   18. Secret Bonus ---See me
#This asks the user's name
user_name = input("What is your name?: ")
#This is the main menu function
def main():
#This asks the user what they want to do
  answer = input("\n"+
   "1. Reverse and display\n" +
   "2. Determine the number of vowels.\n" +
   "3. Consonant frequency.\n" +
   "4. Return first name.\n" +
   "5. Return last name.\n" +
   "6. Return middle name(s).\n"+
   "7. Return boolean if last name contains a hyphen.\n"+
   "8. Function to convert to lowercase.\n"+
   "9. Function to convert to uppercase.\n"+
   "10. Modify array to create a random name (mix up letters).\n"+
   "11. Return boolean if first name is a palindrome.\n"+
   "12. Return full-name as a sorted array of characters.\n"+
   "13. Is this menu!\n"+
   "14. Make initials from name.\n"+
   "15. Return boolean if name contains a title/distinction (“Dr.”, “Sir”, “Esq”, “Ph.d”).\n"
   "16. Quit.\n"
   "\nPick the number of what you want:")
#This runs the program and prints the rturn if the user picks the number
  if answer == '1':
    print(reverse(user_name))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '2':
    print((vowels(user_name)))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '3':
    print((consonant(user_name)))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '4':
    print(firstname(user_name))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '5':
    print(lastname(user_name))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '6':
    print(middlename(user_name))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '7':
    print("7. Do you have a -? " + str(hyphen(user_name)))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '8':
    print(lower(user_name))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '9':
    print(upper(user_name))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '10':
    print(random_name(user_name))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '11':
    print("11. Is your first name a palindrome? " + str(palindrome(user_name)))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '12':
    print(name_sort(user_name))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '14':
    print(initials(user_name))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '15':
    print("15. Does your name contain a title/distinction? " + str(checkfirst(user_name)))
#This runs the program and prints the rturn if the user picks the number
  elif answer == '16':
    print("16. Thanks!")
    quit()
#This runs main after the user picks one to give them the menu again
  main()
#This runs main 
main()