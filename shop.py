shop = []
 
items = input("Items you have bought in shop? ")
items = int(items)
 
for amount in range (items):
    item = input("Find number " + str(amount) + "? ")
    shop.append(item)
print(shop)
 
for item in shop:
    print(item)
print("Item you have " + str(len(shop)) + " items in shop basket list")