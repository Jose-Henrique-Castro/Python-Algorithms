age = int(input("Write your age: "))

if(age < 12):
    print("You will pay R$5.00")

elif(age >= 12 and age <= 17):
    print("You will pay R$8.00")

elif(age >= 18 and age <= 64):
    print("You will pay R$12.00")

else: 
    print("You will pay R$7.00")