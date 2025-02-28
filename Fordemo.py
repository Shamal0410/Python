# For variable in iterable:
#     Statement

'''
range(10): => 0,1,2,3,4,5,6,7,8,9
range(1,10)->1,2,3,4,5,6,7,8,9
range(4,20,3)-> 4,7,10,13,16,19
range(10,1,-1)-> 10,9,8,7,6,5,4,3,2
'''

# To print all numbers from 0 to 9
for no in range(10):
    print(no)

# To print all even numbers from 1 to 100
for no in range(2,101,2):
    print(no)
    
#To print all numbers from 10 to 5 (step operator -1)
for no in range(10,5,-1):
    print(no)

#to print all characters from "Hello World"
for ch in "Hello World":
    print(ch*5)
