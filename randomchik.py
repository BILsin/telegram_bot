import random


def random_number():
    c = []
    fileop = open('music_number.txt')
    musika = int(fileop.readline())
    while len(c) != 5:
        if len(c) == 5: break
        x = random.randomrange(0, musika)
        if c.count(x) == 0:
            c.append(x)
    return c
