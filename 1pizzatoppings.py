#Chapter 6 - Exercise 1
#A loop that prompts the user to enter pizza toppings until they enter a quit value
while True:
    x = input("Enter the list of pizza toppings you'd like to add (Once finished, enter 'quit'): ")
    if x == "quit":
        print("\nThank you, your pizza will be delivered to you soon :)")
        break #End the program when they enter quit
    else:
        print(f"{x.title()} is a good choice!") #The statement prgram says when user enters a topping