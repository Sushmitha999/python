#inserting into a list
def insert_at(x,li,n):
    return li[:n-1]+[x]+li[n-1:]
print(insert_at(6,[1,2,3,4],4))
