myset = set()
print(myset)

myset.add(1)
print(myset)

myset.add(2)
print(myset)
# will not add 2 again. must be unique value
myset.add(2)
print(myset)

mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3]
print(set(mylist))