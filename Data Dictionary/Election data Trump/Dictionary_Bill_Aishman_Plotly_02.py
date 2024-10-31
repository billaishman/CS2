#Name: Bill Aishman
#Description: This code creates a Data Dictionary and displays it in a Plotly bar graph
#Features:
#Log: 1.0

#These import lirbaries Pandas for working with datasets and plotly for displaying plots
import pandas as pd
import plotly.express as px

#Opens a .txt. file and creates arrays
file = open("trump.txt")
line = {}
dictionary = {}
#These are the words to not include from the file
words_remove = ("a", "", "and", "the", "to", "of", "i", "in", "for", "our", "we", "that", "is", "he", "are", "who", "my", "with", "will", "us", "be", "as", "she", "not", "you", "on", "it", "an", "when", "has", "but", "this", "have", "was", "would", "their", "me", "they", "his", "about", "know", "at", "because", "out", "what", "so", "from", "your", "or")
for line in file:
    line = line.replace (".", "").replace (",", "").replace ("-", "").lower()
    line = line.split(" ")
    for words in line:
        if words in dictionary:
            dictionary[words] += 1
        else:
            dictionary[words] = 1
#This creates the dictionary with all the words
dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
#This removes words
for words in words_remove:
    dictionary.pop(words)
#print(dictionary)

#This creates the new dictionary of words
file = open("trump_new.csv", "w")
for key, value in dictionary.items():
        if value > 3:          
            file.write(key + ',' + str(value)+'\n')
file.close() 
#This adds a header for Plotly to use
df = pd.read_csv("trump_new.csv", sep=',', header=None)
df.to_csv("trump_new.csv", header=['words', 'count'], index=False)
df = pd.read_csv('trump_new.csv')
#This uses Plotly to make a bar graph of the instances of the words
fig = px.bar(df, x = 'words', y = 'count', title="Words Trump used in speech")
fig.show()
