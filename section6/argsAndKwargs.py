def myfunc(a,b,c=0,d=0,e=0):
  # returns 5% of the sum of a and b
  return sum((a,b,c,d,e)) * 0.05
myfunc(40,60,100,100)

# user can pass in as many args with *args
# *args returns tuple
def myfunc2(*args):
  return sum(args) * 0.05
myfunc2(40,60,100,100)

def myfunc3(*args):
  for i in args:
    print(i)
myfunc3(40,60,100,100)

# **kwargs returns dictionary
def myfunc4(**kwargs):
  print(kwargs)
  if 'fruit' in kwargs:
    print('My fruit of choice is {}'.format(kwargs['fruit']))
  else:
    print('I did not find any fruit here')
myfunc4(fruit='apple', veggie='lettuce')

def myfunc5(*args,**kwargs):
  print(args)
  print(kwargs)
  print('I would like {} {}'.format(args[0],kwargs['food']))
myfunc5(10,20,30,fruit='orange',food='eggs',animal='dog')

def myfunc6(string):
  output = []
  for letter in range(len(string)):
    if letter % 2 == 0:
      output.append(string[letter].lower())
    else:
      output.append(string[letter].upper())
  return ''.join(output)
print(myfunc6('Incomprehensible'))