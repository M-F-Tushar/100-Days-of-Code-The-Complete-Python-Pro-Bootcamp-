#Length of List
#You can get the length of a list (number of items in the list) or the length of a string (number characters in the string) by using the len() function. https://docs.python.org/3/library/functions.html#len
#IndexError
#When you try to access an item that is not in the range of the List, you will get an IndexError. e.g.

#fruits = ["Cherry", "Apple", "Pear"]
#print(fruits[3]) #This will be an IndexError
#Nested Lists
#You can put Lists inside other Lists, this becomes something called a "Nested List" or a "2D List". e.g.

#fruits = ["Cherry", "Apple", "Pear"]
#veg = ["Cucumber", "Kale", "Spinnach"]
#fruits_and_veg = [fruits, veg]
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
#You could also represent the list in 2D format like this:

#["Cherry", "Apple", "Pear"]
#["Cucumber", "Kale", "Spinnach"]





states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[49])  # No error
print(states_of_america[50])  # IndexError

# Using len() to find the number of items in a List
num_states = len(states_of_america)
print(states_of_america[num_states - 1])


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
# "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)