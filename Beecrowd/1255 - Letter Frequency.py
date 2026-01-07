# -*- coding: utf-8 -*-

N = int(input())

for _ in range(N):
    line = str(input()).lower()
    
    _line = list(line)
    
    line_set = set([letter if letter.isalpha() else "" for letter in _line])
    values = []
    m = 0
    for element in line_set:
        tupla = (element, _line.count(element))
        values.append(tupla)
        if _line.count(element) > m:
            m = _line.count(element)
    
    values.sort(key = lambda x:x[0])
    fstr = ""
    for tupla in values:
        if tupla[1] == m:
            fstr += tupla[0]
    
    print(fstr)
            
        