import random
import numpy as np


def Cal_Final(lam):
    la = 1 / lam
    N = 10000
    t = 480
    total = np.zeros(N)
    arrive = np.zeros(N)
    wait = np.zeros(N)
    start = np.zeros(N)
    process = np.zeros(N)
    end = np.zeros(N)
    ave_wait = np.zeros(N)
    sigma = 2
    u = 10

    for j in range(N):
        i = 0
        arrive[0] = random.expovariate(la)
        wait[0] = 0
        start[0] = arrive[0] + wait[0]
        process[0] = np.random.normal(u, sigma)
        end[0] = start[0] - process[0]

        while start[i] <= t:
            i += 1
            arrive[i] = arrive[i - 1] + random.expovariate(la)
            start[i] = max(arrive[i], end[i - 1])
            wait[i] = max(0, end[i - 1] - arrive[i])
            process[i] = np.random.normal(u, sigma)
            end[i] = start[i] + process[i]
            total[j] += wait[i]
            ave_wait[j] = total[j] / (i + 1)

    final_ave = np.mean(ave_wait)
