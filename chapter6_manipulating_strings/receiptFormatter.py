def receiptFormat(items, left, right):
    print('WELCOME TO CORNER SHOP')
    print('-'*22)
    for k, v in items.items():
        print(k.ljust(left, ' ')+ str(v).rjust(right, ' '))

def total():
    print('-'*22)
    print('TOTAL'.ljust(15, ' ')+ str(result).rjust(5, ' '))
    
    


shoppingList = {'apples': 3.50, 'bread':2.99, 'milk':4.25, 'eggs': 5.00}
result = sum(shoppingList.values())
receiptFormat(shoppingList, 15, 5)
total()
