# indexing
mystring = "Hello World"
print(mystring[-5])

# slicing
print(mystring[2:])
print(mystring[:3])
print(mystring[1:5])
print(mystring[::2])
print(mystring[::-1])

# string properties and methods
x = "Hello World"
print(x.upper())
print(x.split())
print(x.split("o"))

# print formatting with strings
print("My name is {}".format('Zohaib Afridi').upper())
print("My first name is {}, and my last name is {}".format("Zohaib", "Afridi"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
result = 100/777
print(result)
print("The result was {r:1.3f}".format(r=result))
print(f"The result was {result:1.3f}")