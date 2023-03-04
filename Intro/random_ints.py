import random

def randints():
    ints = []
    while 6 not in ints:
        ints.append(random.randint(1, 10))
    return ints