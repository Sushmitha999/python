#duplicate elements of a list
def dup(li,n):
    return [x for x in li for i in range(n)]
print(dup('a',12))
