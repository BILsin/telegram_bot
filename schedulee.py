import random
import sched
import threading
import time


global c


def random_number():
    k = 0
    c = []
    while k != 5:
        if k == 5:
            break
        n = open('music_number.txt')
        X = random.randrange(0, int(n.readline()))
        if c.count(X) == 0:
            c.append(X)
        elif len(c) == 5:
            break
        else:
            continue
    return c


c = random_number()




