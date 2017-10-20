class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.dic = {}
        self.dics = []
    def lisup(self,index):
        self.dics=[self.dics[index]]+self.dics[:index]+self.dics[index+1:]
        # print('===',self.dics)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value=self.dic.get(key)
        if value:
            self.lisup(self.dics.index(key)) #-------------2048---------------------
            return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.dic.get(key): #-------------2048---------------------
            self.lisup(self.dics.index(key)) #-------------2048---------------------
            pass
        else:
            if self.dics.__len__()==self.cap:
                self.dic.pop(self.dics[-1])
                self.dics=self.dics[:-1]
            self.dics.insert(0,key)
        self.dic[key] = value
        # print(self.dics)
        # print(self.dic)
cache=LRUCache(2)
print(cache.put(1,1))            #;)
print(cache.put(2,2))            #;
print(cache.get(1)  )           #//返回1
print(cache.put(3,3))            #; //驱逐钥匙2
print(cache.get(2)  )           #//返回-1（未找到）
print(cache.put(4,4))            #; //驱逐钥匙1
print(cache.get(1)  )           #//返回-1（未找到）
print(cache.get(3)  )           #//返回3
print(cache.get(4)  )           #//返回4
