# -*- coding: utf-8 -*-

N = int(input())

for _ in range(N):
    Values = input().split()
    N1 = int(Values[0])
    D1 = int(Values[2])
    Operador = Values[3]
    N2 = int(Values[4])
    D2 = int(Values[6])
    
    N3 = 0
    D3 = 0
    if Operador == "+":
        N3 = N1*D2 + N2*D1
        D3 = D1*D2
    elif Operador == "-":
        N3 = N1*D2 - N2*D1
        D3 = D1*D2
    elif Operador == "/":
        N3 = N1*D2
        D3 = N2*D1
    elif Operador == "*":
        N3 = N1*N2
        D3 = D1*D2
    N4 = N3
    D4 = D3
    Maior = max(N3,D3)
    while True:
        Found = False
        for i in range(Maior):
            n = i+1
            if(N3 % n == 0 and D3 % n == 0 and n > 1):
                Found = True
                N3 = N3 / n
                D3 = D3 / n
        if Found == False:
            break
    print(f'{N4}/{D4} = {N3:.0f}/{D3:.0f}' )