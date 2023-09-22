import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import sys

N = 1000000  # 1000000次投圈
mv = 5
o = 10
r = 2
R = 4
for i in range(100):
    mv = 10 - i * 0.1
    u, sigma = 1/mv, o
    np.random.seed(i)
    points = sigma * np.random.randn(N, 2) + u
    print(len([xy for xy in points if xy[0] ** 2 + xy[1] ** 2 < (R - r) ** 2]) / N)
