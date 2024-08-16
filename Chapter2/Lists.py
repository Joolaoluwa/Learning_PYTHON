# Example 1, containing a list in python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Example 2, Accessing a list, lets access the first element in the list
#print(bicycles[0])
#print(bicycles[0].title()) #String manipulation on an item in the list

#Example 3, Accessing the last element on the list
print(bicycles[-2])

#Example 4, using individual values from a list
message = "My first bicycle was a " + bicycles[0].title() + "."
#print(message)

#You can use individual values from a list just as you would use any variable

#In python, you can change/modify an item in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'Ducati'
print(motorcycles)

#Adding to a list
cars = ['Toyota', 'Lexus', 'Audi']
# using .append()
# .append() allows you build lists dynamically
# To add elements to the end of a List, use .append()
cars.append("BMW")
print(cars)

# using .insert()
cars.insert(3, "Mikano")
cars.insert(1, 'Volvo')
print(cars)

# Removing from a list
#using del
#To remove an item according to its position in a list use del
del cars[0]
print(cars)

#using .pop()
#To remove an item from the end of a list, thinking of the stack as a stack of items, in which items are popped of at the top of the stack
bmw = cars.pop()
print (cars)
print (bmw)

#Try to always recall that a list is an ordered collection

#You can actually use pop() to remove an item in a list at any position by 
#including the index of the item you want to remove in parentheses.

first = cars.pop(0)
message = "I recently bought a " + first
print(message)