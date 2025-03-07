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
#This imports the csv library
import csv

#This opens the file
infile = open('student_data_cs2.txt', 'r')
#This reads in the lines of file into the list "lines"
lines = infile.readlines() 
#This makes the rows variable
rows = ()
#This opens the file and splits the lines into rows
with open('student_data_cs2.txt') as file:
#This splits the rows
    rows = [line.strip().split() for line in file]
    tuple_rows=tuple(rows)
#This counts how many rows there are in the file
size=len(tuple_rows)
#This gets the column name by taking just the first row of the tuple
column_names = tuple_rows[slice(1)]
#This reads in the whole tuple
tuple_all_rows = tuple_rows[slice(size)]

'''
- ID: 4 characters
- FirstName: 14 characters
- LastName: 14 characters
- Grade: 2 characters
- GPA: 5 characters
- BirthDate: 10 characters
- Gender: 1 character
- ClassRank: 3 characters
- AttendPct: 9 characters
- Honors: 1 character
- Sports: 9 characters
- ClubCount: 8 characters
'''
#This sets the column widths
col_ID = 4
col_FirstName = 14
col_LastName = 14
col_Grade = 2
col_GPA = 5
col_BirthDate = 10
col_Gender = 1
col_ClassRank = 3
col_AttendPct = 9
col_Honors = 1
col_Sports = 9
col_ClubCount = 8

#This opens the output file
outfile = "fixed_length_conversion_Bill_Aishman.csv"
#This writes to the output file
with open(outfile, 'w') as csvfile:
#This writes a csv file 
    csvwriter = csv.writer(csvfile)
#This writes the tuple with all of the rows to the cvs file
    csvwriter.writerows(tuple_all_rows)

#This close the file
infile.close()