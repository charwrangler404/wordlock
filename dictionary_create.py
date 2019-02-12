#!/usr/bin/pythonw

list = open('wordlist.txt', 'r')
dict = open('dictionary.txt', 'w')

for line in list:
    i = 0
    while i < len(line):
        j = i + 4
        dict.write(line[i:j])
        dict.write("\n")
        i = i + 5
        j = j + 5
