# # print("Hello World")
# a=32
# b=32.32
# c=31+41j
# print(a,b,c," ",type(a)," ",type(b)," ",type(c))
# class loops:
#     def forloop():
#         x=int(input("Enter a value-> "))
#         y=int(input("Enter the second value-> "))
#         for i in range(x,y,2):
#             print(i,end=" ")
# loops.forloop()
# array_1=[1,2,3,4,5,6,"test1"]
# print(array_1,type(array_1))
# print(array_1[-1])
# print(array_1,type(array_1))
#Design a Calculator
class Calculator:
    

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
            print(c," is an even number")
        else:
            print(c," is an odd number")
Calculator



 
    
   
