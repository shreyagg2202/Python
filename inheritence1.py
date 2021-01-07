class Cal1:
    def Sum1(self,a,b):
        print("Sum",a+b)

class Cal2:
    def Sub2(self,a,b):
        print("Sub",a-b)

class Cal3(Cal1,Cal2):
    def Mul1(self,a,b):
        print("Mul",a*b)

n1 = int(input("Enter n1="))
n2 = int(input("Enter n2="))

obj = Cal3()
obj.Sub2(n1,n2)
obj.Sum1(n1,n2)
obj.Mul1(n1,n2)
