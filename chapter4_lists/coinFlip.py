import random
coinFlip = random.randint(0,1)
purse = []

if coinFlip == 0:
    coinFlip = "H"
if coinFlip == 1:
    coinFlip = "T"

    for i in range(10):
        i = len(purse)
        purse.append(coinFlip)
        continue
    coinFlip = random.randint(0,1)
    print(*(purse))

