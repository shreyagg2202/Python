num = int(input("Enter the number:"))
temp = num
add=0
while(num>0):
     r = num%10
     add = add*10+r
     num = num//10
if(temp==r):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
    
