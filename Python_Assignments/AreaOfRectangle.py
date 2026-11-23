#write a program which accepts length and width of rectangle and prints Area.

def Area(length,width):
    Ans = length * width
    return Ans

def main():
    Ret = Area(3.5, 4.7)
    print("Are of Rectangle", Ret)


if __name__ =="__main__":
    main()