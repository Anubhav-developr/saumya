num=int(input("enter a digit"))
d=0
p=1
while num!=0:
 d=num%10
 p=p*d
 num=int(num/10)
print(p)   

