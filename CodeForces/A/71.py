#https://codeforces.com/problemset/problem/71/A

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word = input().strip()
    length = len(word)
    if length > 10:
        print(f'{word[0]}{length-2}{word[length-1]}')
    else:
        print(word)