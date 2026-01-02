import random
coinFlip = random.randint(0,1)
purse = []

if coinFlip == 0:
    coinFlip = "H"
if coinFlip == 1:
    coinFlip = "T"
for i in range(10):
 purse.append(coinFlip)
 i += 1
 coinFlip = random.randint(0,1)
 if coinFlip == 0:
    coinFlip = "H"
 if coinFlip == 1:
    coinFlip = "T"
 continue
print(*(purse))
