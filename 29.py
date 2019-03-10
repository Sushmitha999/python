import math
#prime factors and their frequency
def prime(k):
    i=2;
    fac=[]
    while i*i<=k:
        if k%i:
            i+=1
        else:
            k//=i
            fac.append(i)
    if k>1:
        fac.append(k)
    return sorted([fact,fac.count(fact)]for fact in set(fac))
print(prime(130))    
