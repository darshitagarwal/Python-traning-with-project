class calculator:
    def add(a,b):
        return a+b
    def sub(a,b):
         return a-b
    def mul(a,b):
         return a*b
    def div(a,b):
         return a/b
    while(True):
        print("enter 1 to add\n2 to substract\n3 to multiply\n4 to divide\nAny other key to stop")
        x=int(input())
        
        if x!=1 and x!=2 and x!=3 and x!=4:
            break
        a=float(input("a -> "))
        b=float(input("b -> "))
        print("\n")
        if x == 1:
            c=add(a,b)
            print(a," + ",b," = ",c)
        elif x == 2:
            c=sub(a,b)
            print(a," - ",b," = ",c)
        elif x == 3:
            c=mul(a,b)
            print(a," * ",b," = ",c)
        else :
            c=div(a,b)
            print(a," / ",b," = ",c)
        if c%2==0:
            print(c," is an even number\n")
        else:
            print(c," is an odd number\n")
calculator