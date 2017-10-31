arr=[4,1,2,1,5]
while True:
    k=arr.next
    m=arr.next
    print('k:%s,m%s'%(k,m))
    if k==m:
        print('链表有环')
        break
    if k.next:
       k=k.next
    else:
        print('无环')
        break