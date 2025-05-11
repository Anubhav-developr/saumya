def temp():
    choice=int(input("choose the choice  1: for c to f   and 2: for f to c"))
    if choice == 1:
        celsius= int(input("enter celsius value"))
        f=(9/5)*celsius+32
        choice =0
        print("fahrenheit value is")
        return f
    elif choice == 2:
        fahrenheit = int(input("enter fahrenheit value"))
        c=(5/9)*(fahrenheit-32)
        choice = 0
        print("celsius value is")
        return c
    else:
        print("enter a valid keyword")

print(temp())

