#write a program which accepts radius of circle and prints area of circle.

def Area(PI, Radius):
    Ans = (3.14 * Radius * Radius)
    return Ans

def main():
    Ret = Area(3.14, 4.5)
    print("Area of circle:", Ret)

if __name__ =="__main__":
    main()