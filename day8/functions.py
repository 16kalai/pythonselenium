###
#Block of code which only runs when it is called
# 1.parameterised
# 2.Non parameterised
# return
#####


#calling function
def my_world():           #non para
    Animals = ['Lion', 'Tiger', 'Elephant', 'Camel']
    for i in Animals:
        print(i)
    print("Hello")
my_world()                #call a function


#arguments

def my_home(familyname):
    print(familyname +"Natarajan")

my_home("kalaiselvam " )
my_home("kannan " )
my_home("bavani " )


def my_home(familyname, sname):
    print(familyname +"Natarajan " + sname)

my_home("kalaiselvam ", "udayar" )
my_home("kannan ","udayar" )
my_home("bavani ",str(3))           #it will only concatenate 'str'  not 'int'


#passing a list as argument

def my_garden(Trees):
    for t in Trees:
        print(t)
T = ['coconut','mango','jack fruit','banana']
my_garden(T)

# return

def my_relay(r):
    return 5 * r
print(my_relay(4))
print(my_relay(2))
my_relay(1)

def po_list(a):
    return 10 -a
print(po_list(10))
print(po_list(9))

