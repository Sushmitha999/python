#coprime
def gcd(n,m):
    while m!=0:
        n,m=m,n%m
    return n
def coprime(c,d):
    if gcd(c,d)==1:
        print("coprime")
    else:
        print("not coprime")
a, b=[int(x) for x in input("enter:").split()]
coprime(a,b)
    
