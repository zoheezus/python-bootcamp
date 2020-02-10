myfile = open('myfile.txt')
print('first read:\n', myfile.read())
# resetting file read
myfile.seek(0)
print('second read:\n', myfile.read())
myfile.seek(0)

# seperate each line into array index
print(myfile.readlines())

# close file
myfile.close()

# best practice for opening file
with open('myfile.txt') as my_new_file:
  contents = my_new_file.read()
print(contents)

with open('myfile.txt',mode='a') as f:
  f.write('FOUR ON FOURTH')

with open('myfile.txt',mode='r') as f:
  print(f.read())

with open('dafoiweph.txt',mode='w') as f:
  f.write('I CREATED THIS FILE')

with open('dafoiweph.txt',mode='r') as f:
  print(f.read())