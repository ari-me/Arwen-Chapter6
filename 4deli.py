#Chapter 6 - Exercise 4
#Make a list called sandiwch_orders and fill it with a list of sandiwches:
sandwich_orders = ["PB & J Sandiwch", "Grilled Cheese", "Club Sandwich", "Chicken Sandwich", "Hamburger"]
#and an empty list called finished_sandwiches:
finished_sandwiches = [] 
for a in sandwich_orders: #the program will loop through the list
    a = sandwich_orders.pop() #removing each item
    print(f"I made your {a}")
    finished_sandwiches.append(a) #and placing it in the finished_sandiwches list
print(f"\nThese are all of your completed sandiwches: {finished_sandwiches}")