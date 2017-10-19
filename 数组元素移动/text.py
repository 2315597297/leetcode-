def yidong(index):
    return lis[-index:]+lis[:-index]
#这是一个一万长度的lis  将其中所有元素向前或向后移动index位，最后一位元素向前补齐
lis = list(range(1,10))
print(yidong(-6))
print(yidong(1))