# tuples = ( )
# ordered and unchangeable , allows duplicate values
# can store multiple items in single variable

tup = ("kannan", "kalai","bavani","sundu")
print(tup)
print(type(tup))

# access the variable
print(tup[2])

#reverse
print(tup[-2])

#range
print(tup[0:3])
print(tup[:2])
print(tup[2:])

#convert the tuple into list to able to change
x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#add two tuples
t = ("cycle","car","bus","scooty")
s = ("ship",)
t += s
print(t)

#joinining two tuple
tupl = ("vetri","karthi","ram")
tups = (25,29,30)
tup3 = tupl + tups
print(tup3)

#multiply  tuple
print(tup3*2)
f = tup3*2
print(f)

#unpacking
fruits = ("papaya","orange","berry")
(green,yellow,black) = fruits
print(green)
print(black)

#count
k = (1,22,2,3,4,4,5,5,55,6,66,7,77)
l = k.count(5)
print(l)
print(min(k))








