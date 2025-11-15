# -*- coding: utf-8 -*-

import sys

P = "()"
for line in sys.stdin:
    expression = str(line)
    
    __p = ""
    isCorrect = True
    
    for element in expression:
        if __p != element and element in P:
            __p = element
        elif __p == element and element in P:
            isCorrect = False
            break
    
    print("incorrect" if isCorrect else "is correct")
    
    