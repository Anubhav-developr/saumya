s=input('enter a string')
con=0
vowels=0
spaces=0
spc=0
digits=0
for i in s:
    if i.lower() in "aeiou":
      vowels+=1
    elif i.isalpha and i.lower() not in s:    
         con+=1
    elif i.isspace():
         spaces+=1
    elif i.isalnum() not in s:
         spc=spc+1
    else:
      digits=digits+1         
print(vowels,con,spaces,spc,digits)
        