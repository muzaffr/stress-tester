#!/usr/bin/python3

from random import randint as ri, sample, choice

S = 4   # test size, n = 2S
W = 20  # test width, proportional to max(a_i) - min(a_i)
# you are free to modify above parameters
print(S, ri(S * W / 2 - W, S * W / 2 + W))
print(' '.join(map(str, [ri(1, W) for _ in range(S + S)])))
