def merge_and_count(b,c):
    res_arr, inv_count = [], 0
    while len(b) > 0 or len(c) > 0:
        if len(b) > 0 and len(c) > 0:
            if b[0] < c[0]:
                res_arr.append(b[0])
                b = b[1:]
            else:
                res_arr.append(c[0])
                c = c[1:]
                inv_count += len(b)
        elif len(b) > 0:
            res_arr.append(b[0])
            b = b[1:]
        elif len(c) > 0:
            res_arr.append(c[0])
            c = c[1:]

    return res_arr, inv_count

def mergesort(a):
    arr_len = len(a)
    if arr_len <= 1:
        return a, 0
    b,x = mergesort(a[:(arr_len//2)])
    c,y = mergesort(a[(arr_len//2):])
    d,z = merge_and_count(b,c)
    #print(x+y+z)
    return d, x+y+z

lines = [line.rstrip('\n') for line in open('../IntegerArray.txt')]
lines = list(map(int, lines))
#lines = [11, 1, 20, 7]
result = mergesort(lines)[1]
print(result)