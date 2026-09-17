try:
    age = int(input("Write your age: "))
    print(f"age: {age}")

except ValueError:
    print("Write a valid number")