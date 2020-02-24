# starting at 0 ending at 9
mylist = [1, 2, 3]
for i in range(10):
    print(i)
# starting at 3 and ending before 10
for i in range(3, 10):
    print(i)
# step 2 between 3 and before 10
for i in range(3, 10, 2):
    print(i)

print(list(range(0, 11, 2)))

# enumerate
word = 'abcde'
for i, letter in enumerate(word):
    print(i)
    print(letter)
    print('\n')

# zip
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
for i in zip(mylist1, mylist2, mylist3):
    print(i)
print(list(zip(mylist1, mylist2, mylist3)))

# in
print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
print('mykey' in {'mykey': 345})

d = {'mykey': 345}
print(345 in d.values())

mylist = [10, 20, 30, 40, 100]
print(f'the minimum value is {min(mylist)} and the maximum value is {max(mylist)}')

# random
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))
mynum = randint(0,10)
print(mynum)

# user input!
x = float(input('How old are you? '))
print(f'User is {x} many years old')