try:
    dic = {}
    for i in range(5):
        key = input(f"key number {i+1}: ")
        value = input(f"value number {i+1}: ")
        dic[key] = value

    whatKey = input("what key you wanna check: ")
    print(f"The value of the key is: {dic[whatKey]}")

except KeyError:
    print("That key does not exist , try again")