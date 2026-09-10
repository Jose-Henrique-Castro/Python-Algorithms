
list = []

for i in range(7):
    number = input("Read the number: ")
    list.append(number) 

my_set = set(list)
ordered_set = sorted(my_set)

for item in ordered_set:
    print(item)