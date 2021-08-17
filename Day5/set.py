###
# multiple items single variable
# set is a collection of unordered & un indexed
# set = { }
# duplicates are not allowed

set = {"choco","milk","ooats"}
print(set)
print(type(set))

#is present
print("milk" in set)
print("coffee" in set)

# add
set.add("ice")
print(set)

#contains diff
set1 = {"abcd",77,True,40,"male"}
print(set1)
#length
print(len(set1))
print("@@@@@123")

#loop
for i in set1:
    print(i)

#adding list into set
set1 = {"abcd",77,True,40,"male"}
list = ["kiwi","dates"]
set1.update(list)
print(set1)

#do not allow duplicate
set1 = {"abcd",77,True,40,"male",77,"abcd",77}
print(set1)

#remove
set1 = {"abcd",77,True,40,"male"}
set1.remove(77)
print(set1)

#pop
set2 = {"hi","hello","welcome","thanks","gee"}
print(set2)
c = set2.pop()
print(c)

#clear
set2 = {"hi","hello","welcome","thanks","gee"}
set2.clear()
print(set2)

#union
s1 = {"a","b","c"}
s2 = {1,2,3,4,4}
s3 = s1.union(s2)
print(s3)


