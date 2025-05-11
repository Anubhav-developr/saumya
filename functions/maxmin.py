# program to find max min of any input n num
def maxn(num):
 li = []
 maxnum=0
 for i in range(1,num+1):
  inp = int(input("enter number"))
  li.append(inp)
 maxnum=li[0]
 for num in li: 
  if num>maxnum:
   maxnum=num
 print("maximum among all numbers is ",maxnum)
a= int(input("enter number of numbers "))
maxn(a)         