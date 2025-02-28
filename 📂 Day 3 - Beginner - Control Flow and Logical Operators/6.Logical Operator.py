print("Welcome to the rolllercoaster!")
height = int(input("what is your height is cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Child pay $5.")
    elif age <= 18:
        bill = 7
        print("Youth Pay $7.")
    elif 45 <= age <=55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult pay $12.")

    wants_photo = input("Do you want to have a photo take? Take Y for Yes and n for No ")
    if wants_photo == "Y":
        bill += 3 #Add $3 t their bill
    
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grorw taller beore you can ride.")    