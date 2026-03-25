birthdays = {
    "Albert Einstein": "14 March 1879",
    "Isaac Newton": "4 January 1643",
    "Galileo Galilei": "15 February 1564",
    "Marie Curie": "7 November 1867",}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else: 
        print("I don't have birthday information for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")
