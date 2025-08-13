# This is the base or parent class
class Animal:
    def speak(self):
       return "An animal makes a sound."

# This is the derived or child class that inherits from Animal
class Dog(Animal):
    # This method overrides the speak() method from the Animal class
    def speak(self):
        return "Woof!"

# --- Demonstrate Polymorphism ---

# Create an instance of the Animal class
generic_animal = Animal()
print(f"The animal says: {generic_animal.speak()}")

# Create an instance of the Dog class
my_dog = Dog()
# This calls the overridden speak() method in the Dog class
print(f"The dog says: {my_dog.speak()}")

class Cat(Animal):
    def speak(self):
        return "Meow!"
animals=[Dog(),Cat()]
for animal in animals:
       print(animal.speak())
        
           
