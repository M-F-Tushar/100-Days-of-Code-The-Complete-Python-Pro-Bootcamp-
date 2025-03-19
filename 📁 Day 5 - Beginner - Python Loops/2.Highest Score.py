"""
Sum
Python has lots of built-in functions to help us work with numbers. One of them helps us calculate the sum (the total). e.g.

student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores) 
But how does sum() work behind the scenes? The code is written by the people who developed Python and it might look something like this:

student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score
    
print(sum)
PAUSE 1 - Max
There are also a built-in Python methods called max() and min(), which allow you to pass in a List of numbers, and it will give you the highest number or the lowest number.

Your job is to figure out how the Python programmers might have built this functionality using loops and conditionals.

COMPLETE THIS CHALLENGE WITHOUT USING max()
You are given a list of exam scores, and you have to print out the highest score from the List. You will need to use what you have learnt about Lists, For Loops and Conditionals to print out the highest score in the list of student_scores. For example, if the scores were:

8 65 89 86 55 91 64 89
Your code should print

91

"""

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)