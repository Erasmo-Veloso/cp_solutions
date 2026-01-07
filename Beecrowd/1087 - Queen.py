# -*- coding: utf-8 -*-

while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 0 and y1 == 0:
        break
    r = 0
    if x1 == x2 and y2 == y1:
        r = 0
    elif x1 == x2 or y1 == y2 or (x1+y1) == (x2+y2) or (x1-y1) == (x2-y2):
        r = 1
    else:
        r = 2
    
    print(r)
    