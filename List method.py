list1=[]    # Creating an empty list

# append method will add the element at the end of list
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
list1.append(50)
print(list1)

list1.insert(2,100)  # insert(index,element) inserts the element at specified index
print(list1)

list1.sort()
print(list1)

for i in range(4):
    no=int(input("Enter number"))
    list1.append(no)
    
print(list1)
list1.sort()
print(list1)
