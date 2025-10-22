import time

c = 0
stars = "********"
space = " "

while True:
    if c < 15:
     print(space *c + stars)
     c += 1
     time.sleep(0.05)
     if c == 14:
        while c != 0:
         print(space * (c - 1) + stars)
         c -= 1
         time.sleep(0.05)
