#https://codeforces.com/problemset/problem/263/A
import sys
input = sys.stdin.readline
c = 0
r = 0
for i in range(5):
    values = input().split()
    for index, v in enumerate(values):
        v = int(v)
        if v == 1:
            c = index + 1
            r = i + 1
    

print( abs(3-r) + abs(3-c))
