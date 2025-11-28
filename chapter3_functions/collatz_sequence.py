number = int(input("Enter a positive integer to generate its Collatz sequence: "))
while number != 1:
    if number % 2 == 0:
        number = number // 2
        print(number)
    else:
        number = 3 * number + 1
        print(number)
