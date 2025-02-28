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

      
                
 


        
