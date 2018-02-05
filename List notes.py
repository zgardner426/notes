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

