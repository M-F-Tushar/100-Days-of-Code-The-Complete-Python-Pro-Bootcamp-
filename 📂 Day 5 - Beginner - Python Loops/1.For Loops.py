"""
Loops allow us to tell the computer to repeat actions without having to write repeated code. If we wanted the computer to print out 1 through to 100, it would very painful to type a print statement for every number, or even just typing out all the numbers 1 through to 100. Loops allow us to create a rule and the computer can follow it to do a repeated action.

Syntax
for <variable name of each item> in <a List>:
    <do something>
    <do something else> 
PAUSE 1 - Be a Computer
Predict what will be printed from the code below:

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
Indentation
Indentation is very important in Python programming. Every time you see the : symbol used, you need to be careful about the indentation that comes afterwards.

e.g. This code will behave very differently

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
from this code:

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")

"""

fruits = ["Apple", "Peach", "Pearl"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits)

print(fruits)
   