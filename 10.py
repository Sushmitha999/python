#showing count of how many duplicates there are
def pack(list1):
    li=[]
    for i, item in enumerate(list1):
        if i==0 or item!=list1[i-1]:
            li.append([item])
        else:
            li[-1].append(item)
    return li
def dupes(list1):
    return [[len(list2), list2[0]]for list2 in pack(list1)]
list3=['a','a','a','a','b','b','b','c','c','c','c','c','d','d']
print(dupes(list3))
