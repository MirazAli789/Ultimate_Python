# dictionaries in python are key value pairs
# example
dct = {
    "miraz": 97, 
    "lisan": 88, 
    "risan": 83, 
    "surojit": 85
}
print(type(dct))
print(dct)
print(dct.keys())  # returns the keys of the dictionary as a tuple
print(dct.values())  # returns the values of the dictionary as a tuple
print(dct["miraz"])
print(dct.items())  # gives the items of the dictionary using a tuple
dct.update({"ramiz": 78})
print(dct.keys())
print(dct.items())
dct.update({"surojit": 86})
print(dct.items())
print(dct)
print(dct.get("surojit"))
# print(dct.get("laura")) # it returns None when the given key is not present in hte dictionary
# print(dct["laura"]) # it gives error when the given key is not present in hte dictionary
dct.pop("ramiz")
print(dct)
dct.pop("miraz")
print(dct)