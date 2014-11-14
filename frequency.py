#Taking input from the User
phrase = raw_input('Please enter a random phrase:')
print phrase 

#Easy Way -- With Collections 
#Count Letters 
import collections
letters = collections.Counter(phrase) 

#This will print out a dictionary of letter and their freq
print letters

#Counting Words 
#Splits the raw_input and puts into list
listWords = phrase.split()

#This will print a list of the words from raw_input
print listWords 

#Will sort word into Dictionary with frequency
words = collections.Counter(listWords)

#This will print out a dictionary of words and their freq
print words

#this method will include punctuation as part of a word
#if input "bananas! bananas" 
#will output 1 for bananas! and 1 for banana

#More throught out way -- Making a function
#Counting Letters
