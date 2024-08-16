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
print("So sorry to be the bearer of bad news, but the bigger table wont be available to accomodate y'all")
guest1 = guests.pop()
print("Sorry, you're no more invited, " + guest1)
guest2 = guests.pop()
print("Sorry, you're no more invited, " + guest2)
guest3 = guests.pop()
print("Sorry, you're no more invited, " + guest3)
guest4 = guests.pop()
print("Sorry, you're no more invited, " + guest4)
guest5 = guests.pop()
print("Sorry, you're no more invited, " + guest5)
print(guests)
print("Congratulations " + guests[0] + " and " + guests[1] + " you've been invited to the greatest dinner ever")
del guests[1]
del guests[0]
print(guests)