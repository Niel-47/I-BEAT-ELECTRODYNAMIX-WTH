try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    result = num1 / num2
    print("The result of the division is:", result)
except ZeroDivisionError as ex:
    print("Error: Division by zero is not allowed.")
    print("Error details:", ex)
except ValueError as ex:
    print("Invalid input. Please enter valid integers.")
    print("Error details:", ex)
except NameError as ex:
    print("Error: A variable is not defined.")
    print("Error details:", ex)
except:
    print("An unexpected error occurred.")
    import traceback
    traceback.print_exc()
finally:
    print("Execution completed.")
