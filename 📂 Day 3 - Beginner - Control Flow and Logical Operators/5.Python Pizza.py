print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("Do you Want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you wnat extra cheese? Y or N: ")

bill = 0
if size =="S":
    bill += 15
elif size =="M":
    bill += 20
elif size =="L":
    bill += 25
else:
    print("You typed the wrong inputs.")


if pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3

if extra_cheese == "Y":
    bill == 1

print(f"Your final bill is : ${bill}.")