 # to find sum of digits
n=int(input('enter a number'))
s=0
m=n
while n!=0:
 d=n%10
 s=s*10+d                                                                                                                                                                                                                                                                                                                                                                                                                                               `                                                                       `
 n=n//10
if s==m :
 print("pal.")
else:
 print("not a palindrome")
print(s)


