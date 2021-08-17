# if, elif, else statements
#equal ==
# not equal !=
# a <b, a >b, a <=b, a >=b


n = 5
m = 7
if n >m:
    print("n is less than m")   # the condition is not satisfied.........so it will not print
##########
if n <m:
        print("n is less than m") # its fulfilling condition

#Elif
a = 10
b = 5
if a <b:
    print("a is less than b")
elif a ==b:
    print("a is equal to b")
else:
    print("Condition Not satisfied")


## if, elif, else

Total = 50
if Total >=35:
    print("pass")
elif Total<35:
    print("fail")
elif Total >50:
    print("s grade")
else:
    ("absent")

p = 10
q = 20
r = 5
if p <q or q >r:
    print("q is large")
    if r <q or r <p:
        print("r is small")

###
T = 93
E = 87
M = 50
S = 32
SS = 35
if T >50 or T <=59:
    print("E Grade")
elif T <50:
    print("Fail")
else:
    print("Absent")


###
mark = eval((input('Enter your mark:')))
if(mark>=90):
    print('grade:S')
elif(mark>=80):
    print('grade:A')
elif(mark>=70):
    print('grade:B')
elif(mark>=60):
    print('grade:C')
elif(mark>=55):
    print('grade:D')
elif(mark>=50):
    print('grade:E')
else:
    print('Fail')



