def palindrome(list):
    return list==list[::-1]   
list1 = [1, 3, 4, 6, 8, 10, 11, 15]
list2 = ['m','a','l','a','y','a','l','a','m']
if palindrome(list1)==1:
    print("yes")
else:
    print("no")
if palindrome(list2)==1:
    print("yes")
else:
    print("no")
