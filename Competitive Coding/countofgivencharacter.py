#How do you count the occurrence of a given character in a string?
c=0
string=input("Enter the string")
ch=input("Enter the given character")
string1=set(string)
for x in string:
    if(x==ch):
        c=c+1
print("The occurence of",ch,"is:",c)
