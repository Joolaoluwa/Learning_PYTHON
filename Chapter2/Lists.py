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