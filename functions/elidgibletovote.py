#checking person is elidgible to vote or not 
def vote(a):
    if a>=18:
        print("person is  elidgible to vote")
    else: 
        print('person is not elidgible to vote')
age = int(input("enter your age")) 
print("your age is",age,"and")
vote(age)