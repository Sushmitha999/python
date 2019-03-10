import math
#prime factors 
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
    return fac
print(" ".join(str(x) for x in prime(128)))#printing as a string
print(prime(9))
    
