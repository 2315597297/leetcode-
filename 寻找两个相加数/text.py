
lis=list(range(1,1000000))
def getindex(sum):
    '''
    :param sum:在数组中寻找那两个数相加等于这个数  复杂度o(1)
    :return: 这两个数的下标
    '''
    dic={}
    for i in lis:
        dic[i]=i
    for d in dic:
        b=dic.get(sum-d)
        if b:
            return lis.index(d),lis.index(b)
            pass
            #事实证明数据结构有多么的重要，使用离散表比用list快了百倍
    # for i in lis:
    #     for s in lis:
    #         if s==sum-i:
    #             return lis.index(i),lis.index(s)
# 假设有唯一解时  创建一个质数list长度为
print(getindex(999999+999998))