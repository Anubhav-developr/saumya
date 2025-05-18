def sumdigit(a):
    s=0
    while a!=0:
     d=a%10
     s=s+d
     a=a//10
    return s
d=sumdigit(12345645)
print(d) 