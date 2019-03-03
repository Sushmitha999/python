#splitting a list into two parts given length of first part
def split(li,n):
    return li[:n],li[n:]
print(split("computer",4))
