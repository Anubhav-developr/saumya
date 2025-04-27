num=int(input('enter any number'))
d=[]
i=0
while num!=0:
    i=num%10
    num=int(num/10)
    d.append(i)
print(d[0]*d[-1])