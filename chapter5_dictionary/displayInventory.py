inventory = {"sword": 1, "shield": 1, "potion": 5, "gold": 100, "armor": 1}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, str(k))
        item_total = sum(inventory.values())
    print("Total number of items: " + str(item_total))


     

displayInventory(inventory)  
