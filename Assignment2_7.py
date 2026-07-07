# write a program which accept one number and display below pattern . Input = 5 , output = 1 2 3 4 5
#                                                                                          1 2 3 4 5
#                                                                                          1 2 3 4 5
#                                                                                          1 2 3 4 5
#                                                                                          1 2 3 4 5

n = int(input("Enter a number: "))

for i in range(n):
     for j in range(1,n+1):
      print(j, end = " ")
     print()



    

