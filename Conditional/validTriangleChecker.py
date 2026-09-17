def checkTriangle(s1,s2,s3):
    if(side1 + side2 > side3):
        return 1
    elif(side2 + side3 > side1):
        return 1
    elif(side1 + side3 > side2):
        return 1
    else:
        return 0


side1 = float(input("Side 1: "))
side2 = float(input("Side 2: "))
side3 = float(input("Side 3: "))

result = checkTriangle(side1,side2,side3)
if(result):
    print("It is a triangle!")
else:
    print("Not a triangle")


