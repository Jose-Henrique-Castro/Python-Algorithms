# 2 listas 
# converter as 2 listas em sets ( sem duplicatas )
# printar apenas os elementos comuns ( criar outro set )

list1 = [1,"jose",5,"roberto",10,"dafne",18]
list2 = [1,"jose",7,"robertos",10,"dafneh",22]

set1 = set(list1)
set2 = set(list2)

setFinal = set()

setFinal = set(list1).intersection(list2)

for i in setFinal:
    print(i)