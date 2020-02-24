x = 0
while x < 5 :
  print(f'current value of x is {x}')
  x += 1
else :
  print("x IS NOT LESS THAN 5")

# pass
x = [1,2,3]
for i in x :
  pass
print('end of my script')

# continue
mystring = 'Sammy'
for i in mystring :
  if i == 'a' :
    continue
  print(i)

# break
mystring = 'Sammy'
for i in mystring :
  if i == 'a' :
    break
  print(i)

x = 0
while x < 5 :
  if x == 2 :
    break
  print(x)
  x += 1