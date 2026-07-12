#For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.
#Input= 10000
#       20000
#       30000
#      40000
#Display:
#.   Total prime count for each number.


from multiprocessing import Pool

def PrimeNum(no):
    Count=0
    for num in range(2,no+1):  #check every number from 2 to N
        flag = 0 
        
        for i in range(2,num):    #Check the number is divisible by any number
            if num%i == 0:
                flag = 1          #not a prime number
                break
        if flag ==0:              #a prime number
            Count+=1

    print("Input number is: ", no)
    print("Total prime count of number is: ",Count)
    print("-------------------------------------")
    
    return Count


def main():
    Data= [10000,20000,30000,40000]

    Result=[]
    pobj = Pool()
    Result= pobj.map(PrimeNum,Data)
    pobj.close()
    pobj.join()
    

if __name__ =="__main__":
    main()



