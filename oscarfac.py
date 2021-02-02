max=12
min=12
start=1
finish=200


def num_factors(factors):
    return len(factors)
def get_factors(n):
    factors = []
    p=n/2

    for i in range(1, p+1):

        if n % i == 0:
            factors.append(i)
    return factors
for j in range(start, finish):
    n = num_factors(get_factors(j))+1
    if n>=min and n<=max:
        print j,n
