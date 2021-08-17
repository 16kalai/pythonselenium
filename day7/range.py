#  range()

for num in range(10):
    print(num)

for n in range(0,10,3):
    print(n)

#else in for loop

for z in range(10):
    print(z)
else:
    print("finished")

# for else if conditions
for z in range(1,30):
    if z ==11: break
    print(z)
else:
    print("finished")

for z in range(1,30):
    if z ==11: continue
    print(z)
else:
    print("finished")

for z in range(1,30):
    if z ==11: pass
    print(z)
else:
    print("finished")


#nested / inner loop

q = ["we","are","us"]
w = ["together","you","both of"]
for i in q:
    for j in w:
        print(i,j)
