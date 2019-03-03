#drop every nth element from a list
def drop(li,n):
    return [x for i,x in enumerate(li) if (i+1)%n]
print(drop("computer",4))
