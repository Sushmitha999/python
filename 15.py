#run length encoding of a list
from itertools import groupby
def encode(li):
    def aux(k, g):
        l=len(list(g))
        if l>1:
            return [l,k]
        else:
            return k
    return [aux(key,group) for key, group in groupby(li)]
print(encode("aaassssssstttteeee"))
