def receiptFormat(items, left, right):
    print('WELCOME TO CORNER SHOP'.center(28, ' '))
    print('-'*28)
    for k, v in items.items():
        k = k.upper()
        v = "{:.2f}".format(v)
        print(k.ljust(left, ' ')+ str(v).rjust(right, ' '))

def total():
    print('-'*28)
    print('TOTAL'.ljust(20, ' ')+ str(result).rjust(8, ' '))
    print('THANK YOU FOR SHOPPING'.center(28, ' '))
    
shoppingList = {'apples': 3.50, 'bread':2.99, 'milk':4.25, 'eggs': 5.00, 'peanut butter': 6.75, 'chocolate': 3.25, 'broccoli': 4.50, 'potatoes': 1.99, 'chips': 2.50, 'garlic': 1.25  }
result = sum(shoppingList.values())
receiptFormat(shoppingList, 20, 8)
total()
