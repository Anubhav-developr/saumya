#print pallidrome of number
def pallidrome(a):
    s=0
    while a!=0:
        d=a%10
        s=s*10+d
        a=a//10
     if s==a:
         print('number is pallindrome')
     else:
         print('number is not pallindrome')
print(pallidrome(88))