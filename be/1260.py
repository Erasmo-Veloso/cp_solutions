# -*- coding: utf-8 -*-
import sys
N = int(input().strip())

sp_ = input().strip()



for i in range(N):
    Arvores = []
    Arvore_set = {}
    Arvore_tupla = []
    for l in sys.stdin:
        Arvore = l.strip()
        if not Arvore:
            break
        Arvores.append(Arvore)
    Arvore_set = set(Arvores)

    for arvore in Arvore_set:
        print(len(Arvores))
        print(Arvores.count(arvore))
        tupla = (arvore, (Arvores.count(arvore) / len(Arvores))*100)
        Arvore_tupla.append(tupla)

    Arvore_tupla.sort(key=lambda x:x[0])

    for arvore, taxa in Arvore_tupla:
        print(f'{arvore} {taxa:.4f}')