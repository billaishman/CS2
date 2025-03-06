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
import csv

infile = open('student_data_cs2.txt', 'r')
lines = infile.readlines() 
column_names = tuple(lines[0].split())
print(column_names)
print(type(column_names))

with open('student_data_cs2.txt') as file:
    rows = [line.strip().split() for line in file]

outfile = "fixed_length_conversion_Bill_Aishman.csv"
with open(outfile, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)

infile.close()