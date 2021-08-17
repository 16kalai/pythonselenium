## Error handling
# types: 1. compile time error = syntax error
#        2. Logical error = wrong output a/b
#        3. Run time error = int/str

#     Try, Except, Finally

#a = 5
#b = 0
#print(a/b)      #run time error

a = 5
b = 1
k = int(input("Enter the num:"))
print(k)
try:
    print("resource open")
    print(a/b)
except ValueError as e:
    print("invalid input",e)

finally:
    print("resource closed")



