petNames = ["Buddy", "Mittens", "Rex", "Whiskers", "Fido"]
inputName = input("Enter a pet name: ")
if inputName in petNames:
    print( "Yes, " + inputName + " is one of my pets.")
else:
    print( "No, " + inputName + " is not one of my pets.")
