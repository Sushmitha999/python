def flattenList(list1):
    li=[]
    for item in list1:
        if (type(item)==list):
            li.extend(flattenList(item))
        else:
            li.append(item)
    return li   #e.g., [1,[2,3],[4,5]]=>[1,2,3,4,5]
lista = [1, 3, [4, 6], [8, [[10, 11]], 15]]
print(flattenList(lista))
