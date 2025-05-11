#leap year program
def leap(year):
 if (year%4==0) and (year%100!=0 or year%400==0):
  print("year is leap year")
 else:
  print("year is not a leap year")
year=int(input("enter year"))
leap(year)