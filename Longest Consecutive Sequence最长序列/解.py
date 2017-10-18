class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums=set(nums)
        nums=list(nums)
        def getmax(max,i,lis):
            lis.remove(i)
            ji=[]
            ji.append(i)
            tag=True
            mx=0
            mi=0
            mxb=True
            mib=True
            for a in range(1,max):
                if i+a in lis and mxb:
                    ji.append(i+a)
                    lis.remove(i+a)
                    mx+=1
                else:mxb=False
                if i-a in lis and mib:
                    ji.append(i-a)
                    lis.remove(i-a)
                    mi+=1
                else:mib=False
            if not mx+mi+1<max:
                while True:
                    if i+mx+1 in lis and tag:
                        ji.append(i+mx+1)
                        lis.remove(i+mx+1)
                        mx+=1
                    elif i-mi-1 in lis:
                        tag=False
                        ji.append(i-mi-1)
                        lis.remove(i-mi-1)
                        mi+=1
                    else:
                        break

            return ji,lis

        max=1
        max_list=[]
        while True:
            if not nums:
                break
            if nums.__len__()<max_list.__len__():
                break
            m,nums=getmax(max,nums[0],nums)
            if m.__len__()>max_list.__len__():
                max=m.__len__()
                max_list=m
        return max_list.__len__()