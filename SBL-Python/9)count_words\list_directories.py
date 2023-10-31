#Program to count words, lines and characters

lines,words,chars=0,0,0

f=open("Example.txt","r")
for line in f:
    lines+=1
    word=line.split()
    words+=len(word)
    for char in line:
        chars+=1

print(f"Number of lines: {lines}")
print(f"Number of words: {words}")
print(f"Number of characters: {chars}")

import os

files_list=os.listdir('.')

print("The list of files in current folder are:\n")
for file in files_list:
    print(file)
