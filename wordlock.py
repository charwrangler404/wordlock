#!/usr/bin/pythonw

# Define the dials of the lock
dial0 = ['n','b','d','m','j','p','r','s','t','l']
dial1 = ['o','u','y','r','t','l','h','a','e','i']
dial2 = ['t','l','n','a','c','d','e','o','r','s']
dial3 = ['e','d','h','k','y','r','s','t','l','n']

# Open dictionary of words and the combinations file for writing output
dictionary = open('dictionary.txt', 'r')
output = open('combinations.txt', 'w')

# Define function to loop over the dials and test each letter
def test(i, dial, word):
    for letter in dial:
        if word[i] == letter:
            return True
    return False

# Call the test() function against each letter in the word
for word in dictionary:
    if test(0, dial0, word) == True:
        if test(1, dial1, word) == True:
            if test(2, dial2, word) == True:
                if test(3, dial3, word) == True:
                    # Write the combincations to file
                    output.write(word)
