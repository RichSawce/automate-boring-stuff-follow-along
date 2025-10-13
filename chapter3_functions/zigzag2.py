import sys

c = ' '
d = ' ' * 8
reverse = "        "
stars = '********'

while c < d:
   print(c + stars)
   c += ' '
   if c == d and range(len(reverse)):
     for e in range(len(reverse)):
      print(reverse[e:] + stars)
      while c!= d:
       print(c + stars)
       c += ' '
      

        