class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        def is_T(a,b):
            if a[0]<b[0] and a[1]<b[1]:return True
            return False
        def by_y(t):
            return (t[0],t[1])
            pass
        en = sorted(envelopes, key=by_y)
        print(en)
        c=0
        clist=[en[0]]
        for i in en:
            if is_T(clist[-1],i):
                clist.append(i)
        print(clist)



arr=[[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]
s =Solution()
print(s.maxEnvelopes(arr))