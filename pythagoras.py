max=1000000
power=4
sqrt=1/power
for first in range (1,max):
    for second in range (1,max):
        for third in range(1,max):
            result = (first**power+second**power+third**power)**0.25

            if(isinstance(result,int)):
                print first,second,third,result
