
def isSumOf2Squares(n:int):
    for x in range(1,int((n**0.5)//1)+1):
        if ((n-x**2)**0.5).is_integer() and n!=x**2:
            #print(x)
            return True
    return False

count = 0
limit = 1000
for x in range(1,limit+1):
    if isSumOf2Squares(x):
        #print(x)
        count+=1
        

print(f"{count} numbers below {limit} can be expressed as the sum of two square numbers")
