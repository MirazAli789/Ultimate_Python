friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan", None]

print(friends[0])
friends[0] = "Grapes"  # Unlike Strings lists are mutable
print(type(friends))
print(friends[0])
print(friends[1:4])
print(friends)
print(len(friends))
friends.append(45)
print(friends)
print(friends[3])
