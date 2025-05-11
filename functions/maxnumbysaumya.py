#max num oriogram
def maximum(num):
    limx=[]
    maxnum=0
    for i in range(1,num+1):
     c=int(input("enter numbers"))
     limx.append(c)
    maxnum=limx[0]
    for i in limx:
     if maxnum<i:
       maxnum=i
    print(maxnum)
a=int(input())
maximum(a)


    
