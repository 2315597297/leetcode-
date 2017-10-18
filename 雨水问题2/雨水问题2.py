from heapq import *
c =[
  [1,4,3,1,3,2,4,3,3,2,3,4,3,2],
  [3,2,1,3,2,4,4,2,1,5,2,2,2,3],
  [2,3,2,2,3,1,6,4,2,2,2,5,3,1],
  [2,3,3,2,3,1,6,4,3,3,5,5,3,1],
]
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        if len(heightMap) < 3 or len(heightMap[0]) < 3: return 0
        m, n, bd = len(heightMap), len(heightMap[0]), []
        for x, y in zip([0] * n + [m - 1] * n + range(1, m - 1) * 2, range(n) * 2 + [0] * (m - 2) + [n - 1] * (m - 2)):
            heappush(bd, [heightMap[x][y], x, y])
            heightMap[x][y] = -1
        res = 0
        while bd:
            h, x, y = heappop(bd)
            res = self.dfs(h, x, y, bd, heightMap, m, n, res)
            return res

    def dfs(self, h, x, y, bd, heightMap, m, n, res):
        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            if x + dx > 0 and x + dx < m - 1 and y + dy > 0 and y + dy < n - 1 and heightMap[x + dx][y + dy] >= 0:
                tmpH = heightMap[x + dx][y + dy]
                heightMap[x + dx][y + dy] = -1
                if tmpH <= h:
                    res += h - tmpH
                    res = self.dfs(h, x + dx, y + dy, bd, heightMap, m, n, res)
                else:
                    heappush(bd, [tmpH, x + dx, y + dy])
        return res

s = Solution()
c=[[9,9,9,9,9,9,8,9,9,9,9],[9,0,0,0,0,0,1,0,0,0,9],[9,0,0,0,0,0,0,0,0,0,9],[9,0,0,0,0,0,0,0,0,0,9],[9,9,9,9,9,9,9,9,9,9,9]]
print(s.trapRainWater(c))

