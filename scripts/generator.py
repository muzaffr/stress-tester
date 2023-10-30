#!/usr/bin/python3

from random import randint as ri

N = 8
print(1)
print(N)
print(''.join([chr(48 + ri(0, 1)) for _ in range(N)]))
