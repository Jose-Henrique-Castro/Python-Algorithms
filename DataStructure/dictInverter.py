dict1 = {"apple": "red", "banana": "yellow"}

dict2 = {}

for key,value in dict1.items():
    dict2[value] = key


print(dict2)