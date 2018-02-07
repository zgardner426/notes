# Lists

my_list = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_numlist = [8, 4, 7, 5, 2, 9]

print(my_list)
print(my_list[0]) # single index
print(my_list[0:2]) # multiple items, including the first one, not including the last one
# negative indices work but count from the end of the list

# copy of a list
# just creating another variable name for the same object changes afect both my_newlist and my_list
my_newlist = my_list[:]
my_newlist[3] = "Deb"


print(my_newlist)
print(my_list)

# 2d list
my_2dlist = [["Abe", 8], ["Bev", 4], ["Came", 7]]
print(my_2dlist[2] [1])


# If in
if "Cam" in my_list:
    print("Cam is on the list")


# list functions
print(min(my_numlist))  # smallest value
print(max(my_numlist))  # largest value
print(sum(my_numlist))  # sums a list

print(min(my_list))  # for strings order is sorta alphabetical


# list methods
my_list.append("Abe")
print(my_list.count("Abe"))  # finds the number of times an item appeares

my_list.insert(2, "Evelyn")
print(my_list)

my_list.sort()
print(my_list)

my_numlist.sort()
print(my_numlist)

my_numlist.reverse()  # reverse sort
print(my_numlist)

my_list.pop()  # pops off the last item
print(my_list)
my_list.pop(2) # pops off the second item
print(my_list)
first_in_line = my_list.pop(0)  # returns the popped values
print(first_in_line)
print(my_list)

del my_list[0]  # to delete items in a list
print(my_list)

print(my_list.index("Dan"))


# ITERATING A LIST
# make a list from 0 to 9


my_list = []

for i in range(10):
    my_list.append(i)
print(my_list)


# print each item in the list using for each
for num in my_list:
    num += 1
    print(num)
print(my_list) # list itself won't change because list itself wasn't addressed

# add 10 items to each item in the list using iteration
for i in range(len(my_list)):
    my_list[i] += 10 # this would add 10 each time through the list
print(my_list) # now the list is actually changed


# make a d 2d list that is 10 x 10    [[0, 0], [0, 1], [0, 2], ... [9, 9]]
my_list = []
for x in range(10):
    for y in range(10):
        my_list.append([x, y])
print(my_list)

# print ever pair
for pair in my_list:
    print(pair)

# add 10 to each item using iteration
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        my_list[i][j] += 10

print(my_list)


# make a list of numbers 0 to 99 and print it
my_list = []
for i in range(100):
    my_list.append(i)
print(my_list)


# Square every item in the previous list and print it

for i in range(len(my_list)):
    my_list[i] **= 2
print(my_list)

# Show only odd numbers and print it

new_list = []
for i in range(len(my_list)):
    if my_list[i] % 2 == 1:
        new_list.append(my_list[i])

print(new_list)

# Show only numbers from 100 to 1000 and print it
third_list = []
for i in range(len(new_list)):
    if new_list[i] >= 100 and new_list[i] <= 1000:
        third_list.append(new_list[i])
print(third_list)

# Do all four at once

allfour_list = []
for i in range(100):
    num = i ** 2
    if num % 2 == 1:
        if num >= 100 and num <= 1000:
            allfour_list.append(num)

print(allfour_list)

print("\n")
# list comprehension
# [returned_item for iterator in range_or_list filter]

my_list = [x for x in range(100)] # the returned item is x, for ever iteration we are adding x into that list ever 100
print(my_list)

my_list = [x ** 2 for x in range(100)]
print(my_list)

my_list = [x ** 2 for x in range(100) if x ** 2 % 2 == 1]
print(my_list)

my_list2 = [x for x in my_list if x >= 100 and x <= 1000]
print(my_list2)
