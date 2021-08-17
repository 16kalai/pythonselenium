# Any data type :  List, string, set, Dic, tuple
# iterating over a sequence
# key word = for loop

colour =["red","green","yellow","pink"]
for c in colour:
    print(c)

for c in "red":
    print(c)

colour =["red","green","yellow","pink"]
for k in colour:
    print(k)
    if k =="yellow":
        break
colour = ["red", "green", "yellow", "pink"]
for a in colour:
    print(a)
    if a == "green":
        pass

colour =["red","green","yellow","pink"]
for s in colour:
    if s == "green":
        continue           ##it will not print green
    print(s)
