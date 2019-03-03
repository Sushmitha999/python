#extracting a given no. of randomly selected elements from a list
import random
def rnd(li,n):
    return random.sample(li,n)
print(rnd("fandago",3))
