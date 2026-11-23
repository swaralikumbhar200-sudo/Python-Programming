#3. Design a Python application that creates two threads named EvenList and OddList.
#1.Both threads should accept a list of integers as input.
#2.The EvenList thread should:
# - Extract all even elements from the list.
#   - Calculate and display their sum.
# The OddList thread should:
#    - Extract all odd elements from the list.
#   - Calculate and display their sum.
#3.Threads should run concurrently

import threading

def EvenList(no):
    Sum= 0
    for i in no:
        if i%2 == 0:
            print(i)
            Sum = Sum+ i
    
    print("Sum of Even numbers: ", Sum)


def OddList(no):
    Sum= 0
    for i in no:
        if i%2 != 0:
            print(i)
            Sum = Sum+ i
    
    print("Sum of Odd numbers: ", Sum)



def main():
    n=list(map(int,input("enter numbers: ").split()))
    
    thread1 = threading.Thread(target= EvenList, args =(n,))
    thread2 = threading.Thread(target= OddList, args =(n,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ =="__main__":
   main()