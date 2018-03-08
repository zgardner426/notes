# Searching

file = open('data/villians.txt', 'r')

for line in file:
    # strip method removes spaces and \t \n from a string
    print(line.strip())
file.close()


file = open('data/villians.txt', 'r')
for line in file:
    print("hello", line.strip())

file.close()

# We can also write to a file.
'''
file = open('data/villians.txt', 'w') # overwrites the file

file.write("Lee the Merciless")


file.close()
'''

# appending to a file
file = open('data/villians.txt', 'a')  # append to a file

file.write("Lee the Merciless")

file.close

# Read a file into an array (list)

villains = []
file = open('data/villians.txt', 'r')

for name in file:
    villains.append(name.strip())

file.close()
print(villains)

# Linear Search
# find The Infamous Devourer

i = 0
key = "The Infamous Devourer"
while i < len(villains) and villains[i] != key:
    i += 1

# print(key, "is at position", i)
# if it doesn't find it prints at position 100

if i < len(villains):
    print(key, "is at position", i)
else:
    print(key, "is not found")

# Binary Search

key = "Morgiana the Shrew"
lower_bound = 0
upper_bound = len(villains) - 1
found = False

while not found and lower_bound <= upper_bound:
    middle_pos = (upper_bound - lower_bound) // 2
    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos -1
    else:
        found = True
if found:
    print("Found", key, "at the position", middle_pos)
else:
    print(key, "Not found")


import re


# this function takes in a line of text and returns a list of words


def split_line(line):
    return re.findall('[A-Za-z] + (?:\'[A-Za-z]+)?', line)


file = open('data/villians.txt')


all_words = []
for line in file:
    words = split_line(line)
    for word in words:
        all_words.append(word)
print(all_words)

