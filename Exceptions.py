# Exceptions (no problem set, no lab, no stress)


'''
x = 5
print(x/0)
# crashes the program but you don't want that
'''


# Divide by zero error
x = 5
try:
    print(x/0)
except:
    print("you can't divide by zero!")


# Value error
try:
    x = int("A")
except:
    print("Value error, don't use strings")


# File and IOErrors
try:
    file = open("my_file.txt", "r")
except:
    print("problem opening the file")


# print out your error (great for debugging)
try:
    5 / 0
except Exception as e:
    print(e)


# MPG calculator
done = False
while not done:
    try:
        miles = float(input("enter the miles:"))
        gallons = float(input("Enter the gallons:"))
        print(miles / gallons, "MPG")
        done = True
    except ZeroDivisionError:
        print("Enter a non zero number")
    except ValueError:
        print("Please enter a number")
    except Exception as e:
        print(e)
    finally: # not supper usefull for us
        print("This always prints at the end")

# Built in cleanup thing using WITH

with open("data/villians.txt") as f:
    for line in f:
        print(line.strip())

# This automatically closes the file when completed


# High Score

my_score = 100

try:
    with open("data/high_score.txt", "r") as f:
        for line in f:
            high_score = int(line.strip())
    if my_score > high_score:
        with open("data/high_score.txt", "w") as f:
            f.write(my_score)
except Exception as e:
    f = open("data/high_score.txt", "w")
    f.write(str(my_score))
    f.close()


