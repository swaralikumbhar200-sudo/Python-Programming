#id() : ths function is used to show unique address of variables
#if  assign the same value to two different variable, in python they get stored at same location, -Due memory management.
#only if the datatype is imutable.
#address will be different if datatype - Mutable

#example-

a = 10
b = 10

print(id(a))                                       #both a and b value address will be same.
print(id(b))

a = [10]
b = [10]                                           # as it comes under list - Mutable : irrespective of having same value, address will be diff.

print(id(a))
print(id(b))