# map function
def square(num):
  return num**2
my_nums = [1,2,3,4,5]
for i in map(square, my_nums):
  print(i)
print(list(map(square, my_nums)))

def splicer(mystring):
  if len(mystring)%2==0:
    return 'EVEN'
  else:
    return mystring[0]
names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))

# filter function
def check_even(num):
  return num%2==0
mynums = [1,2,3,4,5,6]
# transform to list
print(list(filter(check_even,mynums)))
# iterate through results
for n in filter(check_even,mynums):
  print(n)

# lambdas (anonymous function)
square_lambda = lambda num:num ** 2
print(square_lambda(5))

print(list(map(lambda num:num**2, mynums)))
print(list(filter(lambda num:num%2==0, mynums)))
print(list(map(lambda name:name[0], names)))
print(list(map(lambda x:x[::-1], names)))