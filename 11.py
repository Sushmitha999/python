#run-length encoding with exception
def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for ch in input_string:
        if ch != prev:
            if prev:
                entry = (prev,count)
                lst.append(entry)
            count = 1
            prev = ch
        else:
            count += 1
    else:
        try:
            entry = (ch,count)
            lst.append(entry)
            return (lst, 0)
        except Exception as e:
            print("Exception encountered {e}".format(e=e)) 
            return (e, 1)
 
def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q
 
#Method call
value = encode("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
if value[1] == 0:
    print((value[0]))
    decode(value[0])