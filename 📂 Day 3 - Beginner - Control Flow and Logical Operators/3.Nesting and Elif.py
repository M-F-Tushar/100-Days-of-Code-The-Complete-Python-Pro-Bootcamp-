print("Welcome to the rolllercoaster!")
height = int(input("what is your height is cm?"))

if height >= 120:
    
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    
    if age <= 12:
        print("Please pay $5.")
        
    elif age <= 18:
        print("please Pay $7.")
        
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grorw taller beore you can ride.")    
