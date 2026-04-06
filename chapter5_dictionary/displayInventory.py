inventory = {"sword": 1, "shield": 1, "potion": 5, "gold": 100, "armor": 1}

loot = ["sword", "potion", "gold", "gold", "gem", "gem", "gem"]

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, str(k))
        item_total = sum(inventory.values())
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    addedItems == loot.count(inventory)
    for k in loot:
        inventory[k] = inventory.get(k, 0) + 1
    return inventory
        
        

      
inventory = addToInventory(inventory, loot)  
displayInventory(inventory)
