# function ke andar same function
# syllabus me abhi nahi hai 
def revNumber(num):
    rev=0
    rem=0
    while num>0:
     rem=num%10
     rev=rev*10+rem
     num=num//10
    return rev
print(revNumber(1234))
 