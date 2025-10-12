import sys

#hardcoded zigzag pattern. Second attempt will more closely align with the intended incremental behavior

a = "********"
    
while True:
    print(a)
    try:
        print(" " + a)
        print("  " + a)
        print("   " + a)
        print("    " + a)
        print("     " + a)
        print("      " + a)
        print("     " + a)
        print("    " + a)
        print("   " + a)
        print("  " + a)
        print(" " + a)
    except:
        KeyboardInterrupt
        sys.exit()