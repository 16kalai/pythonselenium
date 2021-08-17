###
# class is like an object constructor or blue print for creating object
# class = keyword
# ###

class first_class:    # class
    x = 5
#object
f = first_class()
print(f.x*3/5)

# __init__() function

class person:                                  #class
    def __init__(self,Name,Age):              #function
        self.name = Name
        self.age = Age
p1 =person("kalai",25)
print(p1.name)
print(p1.age)


