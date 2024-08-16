#Guest List
guests = ['Deborah', 'Daddy', 'Mummy', 'YUY']
print('Welcome to Dinner ' + guests[0])
print('Welcome to Dinner ' + guests[1])
print('Welcome to Dinner ' + guests[2])
print('Welcome to Dinner ' + guests[3])

#Changing the guests List
print(guests[3] + " won't be able to make it")
guests[3] = 'Fortune'

print('Welcome to Dinner ' + guests[0])
print('Welcome to Dinner ' + guests[1])
print('Welcome to Dinner ' + guests[2])
print('Welcome to Dinner ' + guests[3])

#More Guests
print("Dear loved ones, a bigger table has been made available")
guests.insert(0 , "OluwaDara")
guests.insert(3, "Abdul-Lateef")
guests.append("YUY investement")
print(guests)

#Shrinking Guests