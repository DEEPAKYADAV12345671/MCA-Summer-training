#parent class and child class
#class ParentClass:
 #   pass
#class ChildClass(ParentClass):
  #  pass

class Grandfather:
    def __init__(self):
        self.hobby = "Reading the news"
    def speak(self):
        print("I am Grandfather. Hobby:", self.hobby)

class Father(Grandfather):
    def __init__(self):
        super().__init__()
        self.job = "Engineer"
    def speak(self):
        print("I am Father. Job:", self.job)

class Child(Father):
    def __init__(self):
        super().__init__()
        self.school = "ABC School"
    def speak(self):
        print("I am Child. School:", self.school)

# Create objects and call methods
gf = Grandfather()
gf.speak()

ft = Father()
ft.speak()

ch = Child()
ch.speak()
#multiple inheritance
#setter
def depositeBal(self,amount):
    if amount>=0:
        self.__balance+=amount
        return "balane"
    return "Inavlid"
b1=BankAccount("Ramesh",599,13)
print(b1.getBalance(12345))
