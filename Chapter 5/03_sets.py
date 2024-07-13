e = set()  # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54, 5, 5, 5}


print(s)
"""Sets are non indexible"""
s1 = {[1, 2]}  # it is not possible since lists are unhashable
# TypeError: unhashable type: 'list'