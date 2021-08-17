# While loop
# As long as condition is true


q = 15
while q >7:
    print(q)
    q-=1

# break statement
d = 20
while d >15:
    print(d)
    if d ==12:
        break
    d-=1

#continue

o = 30
while o >1:
    o-=3
    if o ==6:
        continue
    print(o)

p = 10
while p >2:
    print(p)
    if p ==5:
        pass
    p-=1

# else stmnt in while loop
h = 2
while h >5:
     print(h)
     h-=1
else:
     print("h is less")
