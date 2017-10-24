
arr=[55,23,3453,451,24,24,345,123,345,243,456,2,43,3465,45,645,6]
# def qsort(L):
#     if len(L) <= 1: return L
#     return qsort([lt for lt in L[1:] if lt < L[0]]) + [L[0]] + qsort([ge for ge in L[1:] if ge >= L[0]])

def qsort(lis):
    if lis.__len__()<=1 : return lis
    a=[]
    b=[]
    #比上面烧稍快
    for i in lis[1:]:
        if i<lis[0]: a.append(i)
        else:b.append(i)
    return qsort(a)+[lis[0]]+qsort(b)
    # return qsort([lt for lt in lis[1:] if lt<lis[0]]) + [lis[0]]+qsort([ge for ge in lis[1:] if ge>=lis[0]])
print(qsort(arr))

