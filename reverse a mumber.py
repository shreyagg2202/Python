n =  int(input("Enter Number"))
sum1 = 0
while(n!=0):
    r = n%10
    sum1 = sum1*10+r
    n = n//10
print("Reverse=",sum1)
