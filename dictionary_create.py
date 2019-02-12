#!/usr/bin/pythonw

list = open('wordlist.txt', 'r')
dict = open('dictionary.txt', 'w')

for line in list:
    i = 0
    j = 4
    while i < len(line):
        dict.write(line[i:j])
        dict.write("\n")
        i = i + 5
        j = j + 5
