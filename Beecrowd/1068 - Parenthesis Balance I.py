# -*- coding: utf-8 -*-

import sys


for line in sys.stdin:
    expression = str(line)
    
    isCorrect = True
    isOpen = False
    isClosed = False
    closed = 0
    opened = 0
    for element in expression:
        if element == "(":
            opened += 1
            isOpen = False if isOpen else True
        elif element == ")":
            closed += 1
            isClosed = False if isClosed else True
    
    isCorrect = (opened == closed) and (isOpen and isClosed)
    print("correct" if isCorrect else "incorrect")
    
    