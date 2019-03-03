#removing kth element from a list
def remove_at(li,n):
    return li[n-1],li[:n-1]+li[n:]
print(remove_at("theory",4))
