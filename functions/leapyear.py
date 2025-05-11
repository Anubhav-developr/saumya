#leap year 
def leapyear(a):
    if a%100==0:
        if a%400==0:
         return 'leap year'
        else:
         return 'not a leap year'
    else:
       if a%4==0:
        return'leap year'
       else:
        return'not a leap year'
a=int(input('enter year'))
print(leapyear(a))
