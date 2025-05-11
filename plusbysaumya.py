def temp():
    choice=int(input('enter your choice'))
    
    if choice==1:
      a=int(input('enter celius value'))
      c=(9/5)*a+32
      return c
    else:
       a=int(input('enter faraneiht value'))
       f=(5/9)*(a-32)
       return f
print(temp())  
      