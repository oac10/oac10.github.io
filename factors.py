def intWithCommas(x):
    if type(x) not in [type(0), type(0L)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)

def isPrime(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           return True

    else:
       return False

counter=2
finalRes=1
target = input("number: ")
while(counter<=target):
    if(isPrime(counter)):
        res=1
        pre=1
        while(res<=target):
            pre=res
            res=res*counter
            if(res>target):
                finalRes=finalRes*pre

    counter=counter+1

#print finalRes
print intWithCommas(finalRes)
