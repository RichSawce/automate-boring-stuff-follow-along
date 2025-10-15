import sys

c = ' '
d = ' ' * 8
reverse = "        "
stars = '********'


while True:
    if c < d:
     print(c + stars)
     c += ' '
    
    if c != d and range(len(reverse)):
      for e in range(len(reverse)):
       try:   
        print(reverse[e:] + stars)
       except:
        KeyboardInterrupt
        sys.exit()
