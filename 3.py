valid = False
while not valid:
    try:
        n=int(input("Enter a number: "))
        while n%2 == 0:
           print(n, "is an even number.")
        valid = True
    except ValueError as ex:
        print("Invalid input. Please enter a valid integer.")
        print("Error details:", ex)
           