try:
    num=int(input("Enter a number: "))
    print(num,"is a valid integer.")
except ValueError as ex:
    print("Invalid input. Please enter a valid integer.")
    print("Error details:", ex)
