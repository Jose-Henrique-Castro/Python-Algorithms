

try:

    n1 = int(input("Write the first number: "))
    n2 = int(input("Write the second number: "))

    division = n1/n2
    print(f"Result: {division}")

except ZeroDivisionError:
    print("You can not divide by 0")

