#gcd
def gcd(n,m):
    while m!=0:
        n,m=m,n%m
    return n
print(gcd(8,2))
