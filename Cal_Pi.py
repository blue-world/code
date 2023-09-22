import math
import random
import numpy as np


def cal_pi(m):
    n = 0
    r = 1
    for i in range(m):
        # x、y为0-r之间的随机数
        x = random.uniform(0, r)
        y = random.uniform(0, r)
        # 若点(x,y) 属于图中1/4圆内 则有效个数+1
        if math.sqrt(x ** 2 + y ** 2) < r:
            n += 1

    # 计算pi
    pi = 4 * n / m
    mv = np.sqrt((np.pi - pi) ** 2)
