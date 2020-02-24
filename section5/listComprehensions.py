mystring = 'hello'
mylist = []
for i in mystring:
  mylist.append(i)
print('mylist[] =', mylist)

# list comprehension version of top block
mylist1 = [i for i in mystring]
print ('mylist1[] =', mylist1)

mylist2 = [x for x in 'word']
print('mylist2[] =', mylist2)

mylist3 = [x for x in range(0,11)]
print('mylist3[] =', mylist3)

mylist4 = [x**2 for x in range(0,11)]
print('mylist4[] =', mylist4)

mylist5 = [x for x in range(0,11) if x%2==0]
print('mylist5[] =', mylist5)

mylist6 = [x**2 for x in range(0,11) if x%2==0]
print('mylist6[] =', mylist6)

# c to f conversion... temp is i
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print('fahrenheit[] =', fahrenheit)

# for loop version of above block
fahrenheit = []
for temp in celcius:
  fahrenheit.append(((9/5)*temp + 32))
print('fahrenheit[] =', fahrenheit)

# if else statement in list comp
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print('results[] =', results)

# nested loops
mylist7 = []
for x in [2,4,6]:
  for y in [1,10,1000]:
    mylist7.append(x*y)
print('mylist7[] =', mylist7)

# same as above block but in list comp
mylist8 = [x*y for x in [2,4,6] for y in [1,10,1000]]
print('mylist8[] =', mylist8)
