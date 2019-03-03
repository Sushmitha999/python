#generating a random permutation of the elements of a list
import random
def per(li):
    li2=list(li)
    random.shuffle(li2)
    return li2
print(per("paradigm"))
