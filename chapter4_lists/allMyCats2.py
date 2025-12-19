import sys

list = []
numOfCats = len(list)
while len(list) <= 6:
 list.append(input("Enter the name of cat " + str(numOfCats + 1) + ": (Or enter nothing to stop)"))
 numOfCats = len(list)
 if not input():
    sys.exit()
 if len(list) == 7:
    print("The cat names are: \n" + str(list))
