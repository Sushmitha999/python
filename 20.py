#rotating a list n places to the left
def rotate(l,n):
    return l[n:]+l[:n]
print(rotate("computer",4))
