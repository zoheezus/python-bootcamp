# for loops basics
mylist = [1,2,3,4,5,6,7,8,9,10]
# for i in mylist:
#   print(i)

for i in mylist:
  # check for even
  if i % 2 == 0:
    print(i)
  else:
    print(f'Odd number: {i}')

list_sum = 0
for i in mylist:
  list_sum += i
print(list_sum)


for i in 'Hello World':
  print(i)

tup = (1,2,3)
for i in tup:
  print(i)

mylist = [(1,2),(3,4),(5,6),(7,8)]
print('length of mylist:',len(mylist))
for i in mylist:
  print(i)
for a,b in mylist:
  print(b)

d = {'k1':1,'k2':2,'k3':3}
for value in d.values():
  print(value)