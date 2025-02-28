weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")
