# -*- coding: utf-8 -*-

import sys

P = "()"
for line in sys.stdin:
    expression = str(line)
    
    __p = ""
    isCorrect = True
    isFounded = False
    for element in expression:
        if __p != element and element in P:
            if not isFounded and element == ")":
                isCorrect = False
                break
            __p = element
            isFounded = True
        elif __p == element and element in P:
            isCorrect = False
            break
    
    print("correct" if isCorrect else "incorrect")
    
    