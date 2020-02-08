# replace index value
my_list = ["one", "two", "three", "four"]
print(my_list)

my_list[0] = "notOne"
print(my_list)

my_list.append("five")
print(my_list)

popped_item = my_list.pop()
print(popped_item)
print(my_list)

my_list.pop(0)
print(my_list)

new_list = ["c","a","d","r","b"]
num_list = [53,32,6,22,88,5]
print(new_list, '\n', num_list)

new_list.sort()
num_list.reverse()
print(new_list, '\n', num_list)