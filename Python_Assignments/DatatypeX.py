# Numeric Data type - int, float, Complex

x = 22
y = 22.89
z = 22+4j

print(type(x))
print(type(y))
print(type(z))

# Text Datatype - Text /string
# by default - it is always string in python
# we use ""/ '' to declare string

x = "Swarali"
print(type(x))


#sequence - list, tuple, range
#list - indicated by [], mutable in nature.
#tuple - indicated by () , imutable in nature.
#range -  needs (start, end, step), mostly used in loops.
#set - set is part set but it looks like sequence. + duplicates are not allowed.

a = [10 ,20, 30, 40, 50 ]
print(type(a))

b = (10 ,20, 30, 40, 50 )
print(type(b))

a = range(1, 8)
print(type(a))
print(len(a))

c = {2, 4, 6, 8}
print(type(c))

#None - here momery is get allocated but value is not defined.
#boolean - works in true or false format.

flag = True
print(flag)
print(type(flag))
print(id(flag))

Age = None
print(Age)
print(type(Age))
print(id(Age))


#dict - we used {} to declare it.
#there is always key value pair in this, key must be unique.

stud = {"name": "Swarali", "Age": 26}
print(type(stud))


#there is also datatype called as binary : which contains two types
#1. byte code
#2. byte array
#not written here, causse not needed
