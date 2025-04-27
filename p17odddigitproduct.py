num=int(input("enter a digit"))
d=0
p=1
i=0
a=[]
while num!=0:
 d=num%10
#  print(i,d)
#  if i%2==0:
 a.append(d)
#   p=p*d
 num=int(num/10)
#  i=i+1

a.reverse()
while i<len(a):
 if i%2==0:
  p=p*a[i]
 i=i+1
print(p)

