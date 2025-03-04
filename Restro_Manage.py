print("Welcome to PYTHON restaurant !...")

menu={
    "tea": 40,
    "pizza":50,
    "burger":80,
    "sandwich":100,
    "pasta": 120,
    "mixveg": 150   
    
}

print("tea: Rs.40\npizza: Rs.50\nburger: Rs.80\nsandwich: Rs.100\npasta: Rs.120\nmixveg: Rs.150")

order_total = 0      

item1 = input(f"Enter the name of item you want to buy:  ")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been added")
    
else:
    print(f"orde item {item1} is not available yet")
 
another_order = input("Do you want to add another item? (Yes/No): ")

if another_order == "Yes":
    item2 = input(f"Enter the item of second order: ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your item {item2} has been added")
    else:
        print(f"Your item {item2} is not available yet")
    
print(f"The total amount of items to pay is {order_total}: ")