import sys
spam = []
cannedSpam = ', '.join(spam[0:-1])
print("Welcome to your shopping list!")
while True:
 inputItem = input("Please enter an item to add to your list (or 'done' to finish): ")
 if inputItem == 'done':
      print("Goodbye!")
      break
 if inputItem == '':
        print("Your list is empty, please enter an item")
 else:
  inputItem != ''
  spam.append(inputItem)
  print("would you like to add anything else to your list?")
  if input().lower == 'no':
      if spam[:] == 1:
         print("Have a nice day\n Your list contains:\n", spam[0])
         sys.exit()
      else:
       print("Have a nice day\n Your list contains:\n", cannedSpam, 'and', spam[-1])


  if input().lower == 'yes' and spam[0]:
        print("So far your list contains:\n", *(spam[0:-1]))
  else:
        input().lower == 'yes'
        print("So far your list contains:\n", *(', '.join(spam[0:-1]), 'and', spam[-1]))
