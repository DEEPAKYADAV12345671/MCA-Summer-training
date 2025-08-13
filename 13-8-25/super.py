class Parent:
    
    def __init__(self, name):
        self.name = name
        print("Parent __init__ called")

class Child(Parent):
    # This is the constructor for the Child class.
    def __init__(self, name, age):
        # Call the constructor of the parent class (Parent) to initialize the name.
        super().__init__(name)
        self.age = age
        print("Child __init__ called")

# Create an instance of the Child class
obj = Child("Rahul", 55)

# You can now access attributes from both Parent and Child
print(f"Object name: {obj.name}")
print(f"Object age: {obj.age}")

 
        