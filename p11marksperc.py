s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())
total = s1+s2+s3+s4+s5
print("total",total)
per = total/5
if per >=90:
    g="A1"
elif per >= 80:
    g="A2"
elif per >= 70:
    g="B1"
elif per >= 60:
    g="B2"
elif per >= 50:
    g="C1"
elif per >= 40:
    g="C2"
elif per >= 33:
   g="D1"
else:
    g="E"
print("total = ",total)
print("percetn",per,"%")
print(g," grade")
 