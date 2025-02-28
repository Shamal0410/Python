# Write a python program to accept a number and print
# whether it is 1 digit,2 digit,3 digit or more than 3 digit number

no=int(input("Enter any number"))
if no>=1 and no<=9:
    print("1 digit number")
else:
    if(no>=10 and no<=99):
        print("2 digit number")
    else:
        if(no>=100 and no<=999):
            print("3 digit number")
        else:
            print("More than 3 digit")
