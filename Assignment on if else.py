# Write a program that prompts the user to input a number and display if the number is even or odd.
no=int(input("Enter any number"))
if no%2==0:
    print("number is even")
else:
    print("number is odd")


#Write a program that prompts the user to input two integers and outputs the largest.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a>b:
    print(a)
else:
    print(b)


#Write a program that prompts the user to input three integers and outputs the largest.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b:
    print(a)
else:
    if b>c:
        print(b)
    else:
        print(c)


#Write a program that prompts the user to input a year and determine whether the year is a leap year or not.
a=int(input("Enter a year"))
if (a%4==0 and a%100!=0) or (a%400==0):
    print("Year is leap")
else:
    print("Year is not leap")


##Write a program that prompts the user to input number of calls and calculate the monthly telephone bills.


calls=int(input("Enter the total telephone calls"))
if calls<100:
    bill=200
elif calls<=150:
    bill=200+(calls-100)*0.60
elif calls<=200:
    bill=200+(50*0.60)+(calls-150)*0.50
else:
    bill=200+(50*0.60)+(50*0.50)+(calls-200)*0.40

print("Your bill : ",bill)    


##Write a program that prompts the user to input the value of a (the coefficient of x2 ), b (the coefficient of x), and c (the constant term) and outputs the roots of the quadratic equation. 
a=int(input("Enter the coefficient of x2"))
b=int(input("Enter the coefficient of x"))
c=int(input("Enter the coefficient of term"))
dis=(b*b)-(4*a*c)
print("Discriminant= ",dis)
if dis==0:
    print("Both roots are equal")
    r1=(-b+math.sqrt(dis))/(2*a)
    print("Root 1: ",r1,"Root 2: ",r2)
elif dis>0:
    print("Both roots are real")
    r1=(-b+math.sqrt(dis))/(2*a)
    r2=(-b+math.sqrt(dis))/(2*a)
    print("Root 1 : ",r1,"Root 2: ",r2)
else:
    print("Both roots are complex")

'''
-b+sqrt(b2-4ac)/2a
-b-sqrt(b2-4ac)/2a
'''


# Write a program that prompts the user to input a number. Program should display the corresponding days to the number.                
a=int(input("Enter a number (1-7) to get corresponding day:"))
if a==1:
    print("Sunday")
else:
    if a==2:
        print("Monday")
    else:
        if a==3:
            print("Thuesday")
        else:
            if a==4:
                print("Wendesday")
            else:
                if a==5:
                    print("Thursday")
                else:
                    if a==6:
                        print("Friday")
                    else:
                        if a==7:
                            print("Saturday")
                        else:
                            print("Invalid input")



# Write a program that prompts the user to input a character and determine the character is vowel or consonant.
a=input("Enter a character")
if a in "aeiou":
    print("vowel")
else:
    print("constant")

      
                
 


        
