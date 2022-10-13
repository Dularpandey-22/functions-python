def calcu(a,b,c):
    i=1
    while i<=a:
        if c=="+":
            print(a+b)
        elif c=="-":
            print(a-b)
        elif c=="*":
            print(a*b) 
        elif c=="%":
            print(a%b)
        else:
            print("I can't do anything with the number")
        break
n=int(input("enter the 1st number"))
m=int(input("enter the 2nd number"))
o=input("enter the operator")
calcu(n,m,o)



# def factorial(x):
#     if x == 1:
#         return 1
#     else: 
#         return(x * factorial(x-1))
# print(factorial(4))   