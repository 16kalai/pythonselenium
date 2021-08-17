#List data type
from typing import List

Animals =['Lion','Tiger','Elephant','Camel']
print(Animals)
#access/replace
print(Animals[1:3])
print(Animals[-2])
print(len(Animals))
#type
print(type(Animals))
#change
Animals[2] = 'Cat'
print(Animals)
Animals[0:1] = ['cow','goat']
print(Animals)
#insert we can insert in position
Animals.insert(1,'Giraffee')
print(Animals)
#append Add= end of the list
Animals.append('bear')
print(Animals)

#Extend list
Birds = ["Dove",'Parrot','Egle',"crow"]
Animals.extend(Birds)
print(Animals)

#remove
Birds.remove('crow')
print(Birds)

#pop specific index
Animals.pop(1)
print(Animals)

#del index position
del Animals[3]
print(Animals)
#looping
for y in range(len(Birds)):
    print(y)
for y in range(len(Birds)):
    print(Birds[y])

#clear
Birds.clear()
print(Birds)

#looping
for x in Animals:
    print(x)

#loop in range
for x in range(len(Animals)):
    print(x)
for x in range(len(Animals)):
    print(Animals[x])

#sort Alphabet
Birds = ["Dove","Parrot","Egle","Crow"]
Birds.sort()
print(Birds)

#decending
Birds.sort(reverse=True)
print(Birds)

#copy
Birds.copy()
print(Birds)
#
L1 = ['a','b','c','d']
L2 = [1,2,3,4,]
L3 = L1 + L2
print(L3)

#append list
for x in L2:
    L1.append(x)
    print(L1)

#extend
L1.extend(L2)
print(L1)
















