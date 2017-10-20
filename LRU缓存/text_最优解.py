from collections import deque


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = deque()
        self.map = {}
        self.timec = 0

    def fix_queue(self):
        while len(self.map) > self.capacity:
            key, val, time = self.queue.pop()
            val_r, time_r = self.map[key]

            if (val == val_r and time_r == time):
                self.map.pop(key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.timec += 1

        if (not key in self.map):
            return -1

        val, _ = self.map[key]
        self.map[key] = (val, self.timec)
        self.queue.appendleft((key, val, self.timec))

        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.timec += 1

        self.map[key] = (value, self.timec)
        self.queue.appendleft((key, value, self.timec))

        self.fix_queue()

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
