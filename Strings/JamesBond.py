name = input("whats your name: ")

name_parts = name.split()

firstName = name_parts[0]
lastName = name_parts[-1]

print(f"The name is {lastName}, {firstName} {lastName}")