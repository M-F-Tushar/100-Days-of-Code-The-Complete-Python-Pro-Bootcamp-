"""
The combination of the range() function with the Python For Loop allows us to run a loop for as many times as we wish. Instead of looping through each item in a List, we can loop through a range of numbers.

Range Function
range(1, 10)

This code doesn't do anything by itself. For example, if you tried to print it, it would not give you individual numbers.

But it can be used in conjunction with For Loops. e.g.

for number in range(1, 10):
    print(number)
This will print out each of the numbers 1 - 9. So the range can also be expressed like this:

a <= range(a, b) < b

Where the range of numbers is inclusive of the lower bound but not inclusive of the upper bound.

PAUSE 1 - The Gauss Challenge
Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.


"""
print(range(1, 10))  # Doesn't do anything

for number in range(1, 10):  # Prints 1 to 9
    print(number)

for number in range(1, 11):  # Prints 1 to 10
    print(number)


# Gauss challenge

total = 0
for number in range(1,101):
    total += number
print(total)