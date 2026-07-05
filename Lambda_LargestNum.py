#write a lambda function which accepts three numbers and returns largest number.

LargestNum= lambda No1, No2, No3 : No1 if (No1>No2 and No1>No3) else No2 if No2>No1 and No2>No3 else No3
Ret= LargestNum(10,50,30)
print("Largest Number is : ", Ret)