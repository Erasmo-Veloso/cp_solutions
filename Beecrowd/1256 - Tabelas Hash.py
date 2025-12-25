# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
    Enderecos, n_Dados = map(int, input().split())
    Map_Hash = {}
    Dados = input().split()
    for Dado in Dados:
        #Posição no Hash
        Dado = int(Dado)
        Posicao = Dado % Enderecos
        #Salvar no Map_Hash
        if Map_Hash.get(Posicao,0) == 0:
            Map_Hash[Posicao] = [Dado]
        else:
            arr = Map_Hash[Posicao]
            arr.append(Dado)
            Map_Hash[Posicao] = arr
            ###Map_Hash[Posicao] = Map_Hash[Posicao].append(Dado)
    
    for K in range(Enderecos):
        str_i = str(K)
        arr = Map_Hash.get(K,[])
        text = ""
        for n in arr:
            n = str(n)
            text += n
            text += " "
            text += "-> "
        print(f'{str_i} -> {text}\\')
    if i+1 != N:
        print()
        