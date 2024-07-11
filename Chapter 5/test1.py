# sets are unordered mutable collection of unique elements
# s = {} # an empty dicitonary
# print(type(s))
# st = set() # empty set
# print(type(st))
# s = {2, 3, 4, 2, "harry", None, True, 3, 4 + 6j}
# print(s, type(s))
# print(s)
# s.add(45)
# print(s)
# s.remove(45)
# print(s)
# print(s.pop())
# print(s)
s1 = {1, 4, 5}
s2 = {2, 3, 3, 4, 4, 5, 5, 6}
print(s1.intersection(s2))
print(s1.union(s2))
print(s1 - s2)
sub = {4, 5}
print(sub.issubset(s1))
print(sub.issubset(s2))
print(s1.isdisjoint(s2))

s3 = {1, 2}
s4 = {3, 4}
print(s3.intersection(s4))
print(s3.isdisjoint(s4))
