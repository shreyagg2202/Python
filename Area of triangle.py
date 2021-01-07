s1 = float(input("please enter the first side = "))
s2 = float(input("please enter the second side = "))
s3 = float(input("please enter the third side = "))
s = (s1+s2+s3)/2
a = ((s*(s-s1)*(s-s2)*(s-s3))**0.5)  
print("Area of triangle is = " a)
