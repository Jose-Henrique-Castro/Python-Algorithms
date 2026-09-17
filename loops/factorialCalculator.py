
def fatorial(number):
    if(number == 0):
        return 1
    return number * fatorial(number-1)

number = int(input("Write a number: "))

final = fatorial(number)
print(f"factorial number is: {final}")


