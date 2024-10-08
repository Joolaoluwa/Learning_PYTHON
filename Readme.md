# TAKING A JOURNEY, to find my footing
# What I want to do

- I'm documenting my python learning process and taking a journey into scripting and automation of tasks
- During this process I will do my possible best to complete a book on python and solve as much problems in this book
- I also want to go into devops ENGINEERING and use python as a primary language to orchestrate and perform IT tasks

# Learning the basics of python

# 6/14/2024
# Agenda: Lists in python, from the book, Python Crash Course

# KEY POINTS TO NOTE WHEN WORKING WITH LISTS IN PYTHON
- A list is used to store a set of information in one place, NO MATTER THE NUMBER
- A list is a "collection" of items in a particular order, it can contain a set of items that don't have any relationship
- To make a list in Python, we use the square brackets ([]), and individual elements in a list are seperated by commas
- Lists are "ordered collections", so you can access any element in the list by telling python what position or index to be accessed. To access an element in a list, you write the name of the list followed by the index of the item to be accessed enclosed in square brackets. In other for you to get the exact position of any number on the list, you subtract one from the current position on the list.
- To access the last element on the list, Python as a special syntax, use -1 as the index
- Most lists you create will be dynamic, meaning you’ll build a list and 
then add and remove elements from it as your program runs its course.
- To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.
- The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list, the new element is added to the end 
of the list
- You can add a new element at any position in your list by using the insert() method. You do this by specifying the index of the new element and the 
value of the new item.
- You can remove an item according to its position in the list or according to its value
- The pop() method removes the last item in a list, but it lets you work with that item after removing it
- The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list
- If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: 
1. When you want to delete an item from a list 
and not use that item in any way, use the del statement
2. You want to use an item as you remove it, use the pop() method.
- Sometimes you won’t know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you 
can use the remove() method.

# Organizing a list
- Often, your lists will be created in an unpredictable order, because you can’t always control the order in which your users provide their data. Although this is unavoidable in most circumstances, you’ll frequently want to present 
your information in a particular order. Sometimes you’ll want to preserve the original order of your list, and other times you’ll want to change the original order.
- Using the sort() method makes it easier to sort a list. The sort method is used to sort a list in either ascending to descending and vice-versa
- To temporarily sort a list we can use the sorted function in order to preserve the original order of the list

# Using Lists