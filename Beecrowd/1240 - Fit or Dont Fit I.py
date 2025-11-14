# -*- coding: utf-8 -*-

N = int(input())

for _ in range(N):
    A, B = input().split()

    start = len(A) - len(B)
    encaixa = False
    
    if len(A) >= len(B):
        encaixa = A[start:] == B

    
    print('encaixa' if encaixa else 'nao encaixa')
        