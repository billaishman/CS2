'''
┌───────────────────────────────────────────────────────────────────────────┐
│                           File Conversion                                 │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Bill Aishman                                                        │
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description: 1. Read in txt file (attached).                              |
|2. Determine columns and their lengths                                     |   
|3. Using the slice function, read data.                                    |
|4. Write file to CSV with your name. Ex)                                   |
|5. Program name: first_last_fixed_length_conversion.py                     |
|6. Upload (or git link) both files.                                        |                             
└───────────────────────────────────────────────────────────────────────────┘
'''
# importing the csv library
import csv
 
# opening the csv file by specifying
# the location
# with the variable name as csv_file
with open('student_data_cs2.txt') as csv_file:
 
    # creating an object of csv reader
    # with the delimiter as ,
    csv_reader = csv.reader(csv_file, delimiter = ',')
 
    # list to store the names of columns
    list_of_column_names = []
 
    # loop to iterate through the rows of csv
    for row in csv_reader:
 
        # adding the first row
        list_of_column_names.append(row)
 
        # breaking the loop after the
        # first iteration itself
        break
 
# printing the result
print("List of column names : ",
      list_of_column_names[0])