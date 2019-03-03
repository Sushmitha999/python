def eliminateDupes(list):
    return list[:1] + [list[i] for i in range(1, len(list)) if list[i-1]!=list[i]]
#first creating a list with head element and concatenating with a list that eliminates duplicates
#
li=[1,1,1,1,1,2,2,5,5,5,5,9,9,9,9,9]
print(eliminateDupes(li))
