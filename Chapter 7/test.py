lst = [1, 78.34, False, "hello", None, 3 + 7j]
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

# tuples are indexible
# i.e tpl[1], tpl[3] .. etc
tpl = (21, 3, 13, 45, 1)
for i in range(0, len(tpl)):
    print(tpl[i])

string = "hello"
print(string[0:5:2])

# range(start,stop,step_size)
for i in range(0,5,2):# it will skip one element
    print(i)
print()
for i in range(0,101,10):
    print(i)
