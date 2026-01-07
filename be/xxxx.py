# -*- coding: utf-8 -*-

N = int(input().strip())


for i in range(N):
    Soldados, Salto = input().split()
    Soldados = int(Soldados)
    Salto = int(Salto)
    original = [i+1 for i in range(Soldados)]
    array = [i for i in range(Soldados)]
    c = 1
    while len(array) > 1:
        array.remove(array[((c*Salto)%len(array))])
        print(c, array[(c*Salto)%len(array)])
        c+=1
        