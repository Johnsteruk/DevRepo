#!/usr/bin/python
#import sys so that we can reference the arguments
import sys
#If I had more time I would check the number of arguments and that the file existed.
inputfile = str(sys.argv[1])
#initialise the word dictionary
wordDict = {}

#read the file into individual lines
with open(inputfile, "r") as file:
       	lines = file.read().splitlines()

       	#loop through the lines
       	for line in lines:
               	#split the line into individual words and store them in a list
               	myList = line.split()
               	for word in myList:
                       	#remove commas and full stops,
                       	#(in a real world example I would put this in a function
                       	#and remove all cases of punctuation)
                       	# I will also force all words to lowercase
                       	#so that we are comparing words that may be at the beginning
                       	#of a sentence. Then add to a dictionary if the word already exists
                       	#then increment the value by 1
                       	if not str(word).replace('.','').replace(',','').lower() in wordDict:
                               	wordDict[str(word).replace('.','').replace(',','').lower()] = 1
                       	else:
                               	wordDict[str(word).replace('.','').replace(',','').lower()] += 1
#sort the dictionary by value in reverse order
sortedDict = {k: v for k, v in sorted(wordDict.items(), key=lambda x: x[1], reverse=True)}

#print the word count
for word in sortedDict:
       	print(sortedDict[word],word)
