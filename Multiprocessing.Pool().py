#Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for 
# every element in the list
#input =[1000000, 2000000, 3000000, 4000000]
#Output =[
#333333833333500000,
# 2666668666667000000,
# ...
#]


from multiprocessing import Pool

def SumSquare(no):
    Total = 0
    for i in range(1,no+1):
        Total+= i*i
        
    return Total



def main():
    n = int(input("Enter a number of elements: "))
    Data =[]
    print("Enter the elements: ")

    for i in range(n):
        Value= int(input())
        Data.append(Value)

    Result= []
    pobj =Pool()
    Result =pobj.map(SumSquare,Data)
    pobj.close()
    pobj.join()

    print("Result is: ", )
    print(Result)

if __name__ =="__main__":
    main()
