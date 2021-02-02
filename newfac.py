max=24
start=1
finish=1000
goodfactors = []
def num_factors(factors):
    return len(factors)
def get_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors
for j in range(start, finish):
    n = num_factors(get_factors(j))

    if n==max:
        goodfactors.append(j)
secondcounter=1
thirdcounter=2
for primary in goodfactors:
    for secondary in range(secondcounter,len(goodfactors)):
        for third in range(thirdcounter,len(goodfactors)):
            if primary!=goodfactors[secondary] and primary!=goodfactors[third] and goodfactors[secondary]!=goodfactors[third]:
                numf = num_factors(get_factors(primary*goodfactors[secondary]*goodfactors[third]))
                print primary,goodfactors[secondary],goodfactors[third],numf
