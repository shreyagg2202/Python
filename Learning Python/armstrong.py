n = input("Enter the number:")
l = len(n)
num = int(n)
temp = num
sum = 0
while(temp!=0):
    r = temp%10
    add = add+r**l
    temp = temp//10

if(add==num):
    print("")
