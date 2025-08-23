print("welcome")
name = "Deepak"
type(name)
age = 23
print(type(age))
weight = 4.5
print(type(weight))  # Fixed: should print the type of weight, not the type function itself

# list datatype
# [val1, val2, val3]
student = ["deepak", 42, 45.66]
print(type(student))

# mapping data types
# dictionary
student1 = {"name": "pak", "age": 56}
print(student1["age"])  # Fixed: use [] to access dictionary values

# sequence data type
# list, tuple, range
# tuple
tuple1 = ()  # Renamed to avoid confusion with built-in 'tuple'

# pop() --> remove item by index
# clear() --> remove all items
# copy() --> copy the list

'''ordered
changeable (mutable)
collection item
allow duplicates
indexing and slicing'''

# create list
fruit = ["apple", "banana"]
# using list function
fruit2 = list(("apple", "banana"))

print(fruit[0:3])
# change elements in list
fruit[1] = "kiwi"
print(fruit)
# adding element
fruit2.append("grapes")
# specific position 
fruit2.insert(1, "orange")
# add multiple elements
fruit2.extend(["pineapple", "watermelon"])  # Fixed: extend expects an iterable, so use a list
print(fruit2)
# remove elements 
# by value (only if exists)
if "mango" in fruit2:
    fruit2.remove("mango")
# by index
fruit2.pop(2)
# last element
fruit2.pop()
# delete the whole list (commented out for safety)
# del fruit2
print(fruit2)  # Now safe to print

# useful methods in list
num = [1, 4, 5, 8, 5, 8, 0, 1]
num.sort()
num.sort(reverse=True)
num.reverse()
print()
print(num)
