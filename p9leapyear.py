year = int(input("enter year"))

if year%100 == 0:
  if year%400==0:
   print("leap yr")
  else:
   print("not a leap year but centrui")
else:
  if year % 4 == 0:
   print("leap year")
  else:
   print("not lp")