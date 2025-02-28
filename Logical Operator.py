# To input three integers and output the largest.

a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b and a>c :
    print(a)
else:
    if b>c :
        print(b)
    else:
        print(c)
