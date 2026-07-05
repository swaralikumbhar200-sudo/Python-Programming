# write a lambda function which accepts one number and returns True if divisible by 5.

CheckDivisible= lambda No : True if No % 5 ==0 else False
Ret = CheckDivisible(22)
print("Divisible by 5:", Ret)