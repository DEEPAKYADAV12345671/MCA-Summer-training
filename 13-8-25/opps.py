#oops
#it is a paradigm that organise software design around object
#key concepat of opps
#class
#objects(instance)
#attributes(function inside the class)
#methos(function inside class)
#classes and objects
#general syntax of class
#class Classname:
#class Student:
    #Student1={"name":"Rohan","age":12,"course":"Mern"}
    #Student2={"name":"sohan","age":12,"course":"Mern"}
    #Student3={"name":"mohan","age":12,"course":"Mern"}
    #templete or class
class Student:
    # Constructor will initialise an object and attach properties duender funtion
    def __init__(self, name, age, course):
        self.name = name#self refrence the object [properties]
        self.age = age
        self.course = course

# Creating an object (instance) of Student
s1 = Student("rohan", 12, "mern")

# Example: print attributes
print(s1.name)
print(s1.age)
print(s1.course)
#there are two types of variable that
#class variable & instance, variable,object,identifier
def __str__(self):
        return f"Student(name={self.name}, age={self.age}, course={self.course})"

# Creating an object (instance) of Student
s1 = Student("rohan", 12, "mern") 
def__str__(self):
return"hello"
s1=Student("Rihan",12,"Mern")
print(s1)
#format string
#methods 
def greet(self):
     print("welcome",self.name)
     s1=Student("Shubham",12,)