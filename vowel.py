p = input("")
vowels = 0
for i in p:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels=vowels+1
if(vowels!=0):
    print("It has a vowel")
else:
    print("It does not have a vowel")
    
