#Chapter 6 - Exercise 2
#A movie theater program that tells the price depending on a person's age
print("Welcome to the Movies!")
while True: #To loop the program over and over
    age = int(input("Enter the person's age: ")) #asking the person's age
    if age < 3: #If they are less than 3, the price is 0
        print("Ticket Price: 0$")
    elif age >= 3 and age < 12: #If they are 3-11, the price is 10$
        print("Ticket Price: 10$")
    else: #If they are 12+, the price is 15$
        print("Ticket Price: 15$")