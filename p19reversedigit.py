s=0
#input 123
# n=123 which is not eual to 0 therefore , enter in loop 
# d= 123%10 whcih is 3 , s=0*10+d === s=3 now n= 123/10 whcih is 12 now 12 not equal to 0 there fore again enter in loop d=12%10 whcih is 2 now s=3*10+2 === 32 12/10 ==1 and 1 not eql to 0 enter loop d=1%10==0 s=32*10+1=321 now n=0 end loop then print s whivch is 321

n=int(input("enter a number"))
while n!=0:
 d=n%10 
 s=s*10+d   
 n=int(n/10)
print(s)
 
 
