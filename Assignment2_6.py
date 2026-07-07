# write a program which accept one number and display below pattern. input=5 , output=  * * * * *
#                                                                                       * * * * 
#                                                                                       * * * 
#                                                                                       * * 
#                                                                                       *   

n= int(input("Enter a number: "))

for i in range(n,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()
    

        

    
