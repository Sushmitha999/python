#a list of sublists
def pack(list1):
    li=[]
    for i, item in enumerate(list1):
        if i==0 or item!=list1[i-1]:
            li.append([item])
        else:
            li[-1].append(item)
    return li
list2=[1,1,1,1,2,2,2,4,4,4,4,4,7,7,7,7,7,7,7]
print(pack(list2))
