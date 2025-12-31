import sys
spam = []
cannedSpam = ', '.join(spam[0:-1])
print("Welcome to your shopping list!")
while True:
    inputItem = input(
        "Please enter an item to add to your list (or 'done' to finish): ")
    if inputItem == 'done':
        print("Goodbye!")
        break
    if inputItem == "":
        print("You must enter an item")

    else:

        inputItem != "" and 'done'
        spam.append(inputItem)
        while True:
            inputItem = input(
                "would you like to add anything else to your list?\n")

            if inputItem.lower() == 'no' and spam[0:]:
                print("Have a nice day1\n Your list contains:\n", *(spam))
                sys.exit()


            if inputItem.lower() == 'no' and spam[0:]:
                print("Have a nice day2\n Your list contains:\n", *
                      (', '.join(spam[0:-1]), 'and', spam[-1]))
                sys.exit()


            if inputItem.lower() == 'yes' and spam[0]:
                print("So far your list contains:\n", *(spam))
                break

            else:
                inputItem.lower() == 'yes' and spam[0:]
                print("So far your list contains:\n", *
                      (', '.join(spam[0:-1]), 'and', spam[-1]))
                break
