# 最初，位置（0，0）有一个机器人。给定一系列的动作，判断这个机器人是否产生一个圆圈，这意味着它返回原来的位置。
# 移动序列由字符串表示。每个动作都由一个角色代表。有效的机器人移动是R（右），L（左），U（上）和D（下）。
# 输出应为true或false，表示机器人是否制作圆。
# 示例1：
# 输入： “UD”
#  输出： true
# 示例2：
# 输入： “LL”
#  输出： false

# 注意  此题有歧义，不是过程中创建了圆圈就算赢，必须要最后回到原点才算，太简单了，提交的实例都不够

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lis=list(moves)
        x=0
        y=0
        for m in lis:
            if m == 'R':
                x-=1
            elif m == 'L':
                x+=1
            elif m == 'U':
                y+=1
            elif m == 'D':
                y-=1
        return y==x==0