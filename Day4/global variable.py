#created outside a function = Global variable
#created inside a function = Local variable
#global varibale we can use both inside/outside a function

#global variable
X = "Awesome"

def myfun():
    print("python is",X)

myfun()

#Local variable

V = "Vetri"
def myfun():
    V = "selvan"
    print("Handsome guy" + V)
myfun()
print("Handsome guy" + V)

#Global key word
        #outside fun
def mygo():
    global k
    k = "class"
mygo()
print(k)


