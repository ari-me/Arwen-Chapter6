#Chapter 6 - Exercise 5
#The same list in chapter 4 except added pastrami sandwich. The pastrami has run out
sandwich_orders = ["PB & J Sandiwch", "Pastrami", "Grilled Cheese", "Club Sandwich", "Pastrami", "Chicken Sandwich", "Hamburger", "Pastrami"]
finished_sandwiches = []
print("The deli has run out of pastrami.")
#This is the loop to remove pastrami from the sandwich_order list:
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
for a in sandwich_orders[:]:
    a = sandwich_orders.pop()
    print(f"I made your {a}")
    finished_sandwiches.append(a)
print(f"\nThese are all of your completed sandiwches: {finished_sandwiches}")