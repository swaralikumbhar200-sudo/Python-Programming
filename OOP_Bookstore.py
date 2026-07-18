#Write a Python program to implement a class named BookStore with the following specifications:
#1.The class should contain two instance variables:
        #1.Name (Book Name)
        #2.Author (Book Author)
#2.The class should contain one class variable:
     # NoOfBooks (initialize it to 0)
#3.Define a constructor (__init__) that accepts Name and Author and initializes the instance variables.
#4.Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
#5.Implement an instance method:
# Display()
#Should display the book details in the following format:
#<BookName> by <Author>. No of books: <NoOfBooks>

#Example Usage
#Obj1 = BookStore("Linux System Programming", "Robert Love")
#Obj1.Display()
# Linux System Programming by Robert Love. No of books: 1

#Obj2 = BookStore("C Programming", "Dennis Ritchie")
#Obj2.Display()
# C Programming by Dennis Ritchie. No of books: 2

class BookStore:
    NoOfBooks = 0

    def __init__(self,name,author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.Name, "by", self.Author)
        print("No of books: ", BookStore.NoOfBooks)


obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.Display()

obj2 = BookStore("C Programming", "Dennis Ritchie")
obj2.Display()