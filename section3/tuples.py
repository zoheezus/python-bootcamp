mytuple = (1,2,3)
print(type(mytuple))
mylist = [1,2,3]
print(type(mylist))

t = ('a','a','b')
print(t)
print(t.count('a'))
print(t.index('a'))

# lists are mutable
mylist[0] = 'NEW'
print(mylist)

# tuples are immutable
# mytuple[0] = 'NEW'
# print(mytuple)