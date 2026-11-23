# Design a Python application that creates two threads named EvenFactor and OddFactor.
#1.Both threads should accept one integer number as a parameter.
#2. The EvenFactor thread should:
#   - Identify all even factors of the given number.
#   - Calculate and display the sum of even factors.
#3. The OddFactor thread should:
#   - Identify all odd factors of the given number.
#   - Calculate and display the sum of odd factors.
#4. After both threads complete execution, the main thread should display the message:
#  "Exit from main"



import threading

def EvenFactor(no):
   Sum=0
   for i in range(1,no+1):
      if no%i ==0  and i%2 ==0:
         print(i)
         Sum = Sum+ i

   print("sum of even factors is: ", Sum)
   

def OddFactor(no):
   Sum=0
   for i in range(1,no+1):
      if no%i ==0  and i%2 !=0:
         print(i)
         Sum = Sum+ i

   print("sum of odd factors is: ",Sum)




def main():
    n=int(input("Enter a number: "))
    
    thread1 = threading.Thread(target= EvenFactor, args =(n,))
    thread2 = threading.Thread(target= OddFactor, args =(n,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    
    print("Exit from Main")

if __name__ =="__main__":
   main()