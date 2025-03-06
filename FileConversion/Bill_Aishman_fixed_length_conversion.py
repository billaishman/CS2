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


'''
def slice_columns_from_text(file_path, column_widths, column_names):
    """
    Slices columns from a text file based on provided column widths.

    Args:
        file_path (str): Path to the text file.
        column_widths (list): List of integers representing column widths.
        column_names (list): List of strings representing column names.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row
              and contains the sliced data with column names as keys.
    """
    results = []
    with open(file_path, 'r') as file:
        for line in file:
            row_data = {}
            start = 0
            for i, width in enumerate(column_widths):
                end = start + width
                column_data = line[start:end].strip()
                row_data[column_names[i]] = column_data
                start = end
            results.append(row_data)
    return results


'''
infile.close()