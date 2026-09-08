def calculate(num1,num2,operator):
    if(operator == "+"):
        sum = num1 + num2
        return sum
    elif(operator == "-"):
        sub = num1 - num2
        return sub
    elif(operator == "/"):
        div = num1 / num2
        return div
    else:
        mult = num1 * num2
        return mult


num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))
operator = str(input("Operator : "))

result = calculate(num1,num2,operator)
print(result)