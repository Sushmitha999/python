#run-length encoding
from itertools import groupby
def encode(alist):
    return [[len(list(group)), key] for key, group in groupby(alist)]
print(encode("aaaabbbbcccc"))
