# -*- coding: utf-8 -*-

N = int(input())

for _ in range(N):
    f = float(input())
    d = 0 
    while f > 1:
        f /= 2
        d+=1
    print(f'{d} dias')
        