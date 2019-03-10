#euclid's totient function
def gcd(n,m):
    while m!=0:
        n,m=m,n%m
    return n
def coprime(c,d):
    return gcd(c,d)==1
def phi(k):
    if k==1:
        return 1
    else:
        r=[n for n in range(1,k) if coprime(k,n)]
        return len(r)
print(phi(128))
    
