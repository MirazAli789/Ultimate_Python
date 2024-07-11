# # python dictionaries are unordered mutable key-value pairs
# marks = {"a": 12, "b": 8, "c": 31, "d": 90, "e": 91}
# print(type(marks))
# print(marks)
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks.get("a"))
# marks.pop("a")
# print(marks)
# marks.pop("d")
# print(marks)
# print(marks.get("d"))
# print(marks["d"])
d = {}
print(type(d))  # <class 'dict'>
s = set()
print(type(s))
s.add(12)
s.add(3)
s.add(6)
s.add(18)
s.add(10)
s.add(54)
print(s)
s.remove(54)
s1 = {12, 4, 1, 34, 12, 14}
s2 = {4, 114, 5, 634, 12, 41, 34}
print(s2.issubset(s1))
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.isdisjoint(s2))
print(s1.pop())
