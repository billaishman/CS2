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


import random

#   1. This function will reverse and display a user input
def reverse(x):
  reverse_name = x[::-1]
  print("1. Your name in reverse is " + reverse_name)

#   2. This function will determine the number of vowels and then create subtotals of each.
def vowels(x):
  a_count = e_count = i_count = o_count = u_count = vowel_count = 0
  for char in x:
    if char == 'a' or char == 'A':
      a_count += 1
      vowel_count +=1
    if char == 'e' or char == 'E':
      e_count += 1
      vowel_count +=1
    if char == 'i' or char == 'I':
      i_count += 1
      vowel_count +=1
    if char == 'o' or char == 'O':
      o_count += 1
      vowel_count +=1
    if char == 'u' or char == 'U':
      u_count += 1
      vowel_count +=1
  print("2. There are " + str(a_count) + " a's in your name. \n2. There are " 
        + str(e_count) + " e's in your name. \n2. There are " 
        + str(i_count) + " i's in your name. \n2. There are " 
        + str(o_count) + " o's in your name. \n2. There are " 
        + str(u_count) 
        + " u's in your name. \n2. There are " + str(vowel_count) + " total vowels in your name.")

#   3. Consonant frequency. Bonus: Subtotals of each consonant
def consonant(x):
  b_count = c_count = d_count = f_count = g_count = h_count = j_count = k_count = l_count = m_count = n_count = p_count = q_count = r_count = s_count = t_count = u_count = v_count = w_count = x_count = y_count = z_count = consonant_count = 0
  for char in x:
    if char == 'b' or char == 'B':
      b_count += 1
      consonant_count +=1
    if char == 'c' or char == 'C':
      c_count += 1
      consonant_count +=1
    if char == 'd' or char == 'D':
      d_count += 1
      consonant_count +=1
    if char == 'f' or char == 'F':
      f_count += 1
      consonant_count +=1
    if char == 'g' or char == 'G':
      g_count += 1
      consonant_count +=1
    if char == 'h' or char == 'H':
      h_count += 1
      consonant_count +=1
    if char == 'j' or char == 'J':
      j_count += 1
      consonant_count +=1
    if char == 'k' or char == 'K':
      k_count += 1
      consonant_count +=1
    if char == 'l' or char == 'L':
      l_count += 1
      consonant_count +=1
    if char == 'm' or char == 'M':
      m_count += 1
      consonant_count +=1
    if char == 'n' or char == 'N':
      n_count += 1
      consonant_count +=1
    if char == 'p' or char == 'P':
      p_count += 1
      consonant_count +=1
    if char == 'q' or char == 'Q':
      q_count += 1
      consonant_count +=1
    if char == 'r' or char == 'R':
      r_count += 1
      consonant_count +=1
    if char == 's' or char == 'S':
      s_count += 1
      consonant_count +=1
    if char == 't' or char == 'T':
      t_count += 1
      consonant_count +=1
    if char == 'v' or char == 'V':
      v_count += 1
      consonant_count +=1
    if char == 'w' or char == 'W':
      w_count += 1
      consonant_count +=1
    if char == 'x' or char == 'X':
      x_count += 1
      consonant_count +=1
    if char == 'y' or char == 'Y':
      y_count += 1
      consonant_count +=1
    if char == 'z' or char == 'Z':
      z_count += 1
      consonant_count +=1

  print("3. There are " + str(b_count) + " b's in your name. \n3. There are " + 
        str(c_count) + " c's in your name. \n3. There are " + 
        str(d_count) + " d's in your name. \n3. There are " +
        str(f_count) + " f's in your name. \n3. There are " + 
        str(g_count) + " g's in your name. \n3. There are " + 
        str(h_count) + " h's in your name. \n3. There are " + 
        str(j_count) + " j's in your name. \n3. There are " +
        str(k_count) + " k's in your name. \n3. There are " + 
        str(l_count) + " l's in your name. \n3. There are " + 
        str(m_count) + " m's in your name. \n3. There are " + 
        str(n_count) + " n's in your name. \n3. There are " +
        str(p_count) + " p's in your name. \n3. There are " + 
        str(q_count) + " q's in your name. \n3. There are " + 
        str(r_count) + " r's in your name. \n3. There are " + 
        str(s_count) + " s's in your name. \n3. There are " +
        str(t_count) + " t's in your name. \n3. There are " + 
        str(v_count) + " v's in your name. \n3. There are " +
        str(w_count) + " w's in your name. \n3. There are " + 
        str(x_count) + " x's in your name. \n3. There are " +
        str(y_count) + " y's in your name. \n3. There are " + 
        str(z_count) + " z's in your name. \n3. There are " + 
        str(consonant_count) + " total consonants in your name.")

#   4. This function will print the first name entered.
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

user_name = input("What is your name?")
print("Your name is " + user_name)
reverse(user_name)
vowels(user_name)
consonant(user_name)
