# Write a program in Python that reads data values as product name and price. For this, it asks user to
# enter such data pairs until user says 'n'/no. Store these data in a dictionary whose keys are the product names and whose values are the prices. 
# When the user is done entering products and prices, allow them
# to enter a product name and print the corresponding price or a message if the product is not in the data.
# Also, allow the user to enter price range and print out all the products whose price is within that range.
# Take at least 8 such data

product = {}
print("Enter the product and price: ")
print("Enter 'n' to stop entering: ")
while(True):
    x = input("Product name: ")
    if(x == 'n'):
        break
    y = int(input("Price: "))
    product[x] = y
    
print()
# print items of dictionary
for name, price in product.items():
    print(f"{name}: {price} Rs")


# When the user is done entering products and prices, allow them
# to enter a product name and print the corresponding price or a message if the product is not in the data.

print("\nEnter item name and know price: ")
item_enter = input("Enter item name: ")
if item_enter not in product:
    print("Item not present")
else:
    item_price = product[item_enter]
    print(f"Price of {item_enter}: {item_price}")



# Also, allow the user to enter price range and print out all the products whose price is within that range.

print("\nEnter proce range: ")
start = int(input("Enter first range: "))
end = int(input("Enter end range: "))

print("\Product within given range: ")

for name, price in product.items():
    if(price >= start and price <= end):
        print(f"{name}: {price} Rs")
    




