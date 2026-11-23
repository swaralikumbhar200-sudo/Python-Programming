# write a lambda function which accepts one number and returns True if the number is Even otherwise false.

CheckEven= lambda No : True if No%2==0 else False
Ret = CheckEven(100)
print("Even Number : ", Ret)