import math
import time
def sieve(n):
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
def primeSum(n):
    p=2
    limit=math.floor(n/2)
    for p in primes:
        q=n-p
        if(p>q):
            break
        if(q in primes):
            out.extend([p,q])
    print (n,"has",round(len(out)/2),":")
    for i,j in zip(out[0::2],out[1::2]):
        print (i,"+",j,sep='')

    print ("")

primes = sorted(set(sieve(32000)))
for __ in range(int(input())):
    out = []
    primeSum(int(input()))
"""input format:
2: number of test cases
20
100"""
