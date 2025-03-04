s1="Hello World"

#s1
#-11            -3 -2-1
#H e l l o   W o r l d 
#0 1 2 3 4 5 6 7 8 9 10


print(s1)
print("Length : ",len(s1))
print("character at 0 index : ",s1[0])
print("character at 7 index : ",s1[7])

#Slicing
#s1[startindex:endindex]

print("slicing from 2 to 8 ",s1[2:8])
print("slicing from 1 to 9 with step 2 :",s1[1:9:2])

# if end index is not given then it will print upto last character
print("slicing from 2 ",s1[2:])

#if start index is not given then it will print from 0th index
print("slicing upto 8 ",s1[:8])

print(s1[9:1:-1])

print("Reverse ",s1[::-1])
