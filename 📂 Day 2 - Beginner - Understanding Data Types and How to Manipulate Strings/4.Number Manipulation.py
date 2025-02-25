bmi = 84 / 1.65 ** 2
print(bmi)

# Flooring a number( Remove all decimal places)
print(int(bmi))

# Rounding a number( Round the decimal number to the nearest whole number) 
print(round(bmi))

print(round(bmi, 2))

# F-Strings = In Python we can use insert a variable or an expression into a string

score = 0
height = 1.8
is_winning = True

print(f"your score is = {score}, your height is {height}, you are winning is {is_winning}")
