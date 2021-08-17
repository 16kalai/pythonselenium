###
# object can also contain methods
# Methods in objects are functoins that belongs to the object
# self parameter is a reference to the current instance of the class, it is also used to access variables that belongs to the class
# ###

class person:                                  #class
    def __init__(self,Name,Age,Gender):              #function
        self.name = Name
        self.age = Age
        self.gender = Gender
    def myfun(self):
        print("Hello,.My name is:" + self.name)
        print("Hi I am:" + self.age)

p1 = person("kalai","27","Male")
p1.myfun()


