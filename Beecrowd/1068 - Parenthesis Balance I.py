# -*- coding: utf-8 -*-

P = "()"

expression = str(input())

__p = ""
isCorrect = True

for element in expression:
    if __p != element and element in P:
        __p = element
    elif __p == element and element in P:
        isCorrect = False
        break

print("is correct" if isCorrect else "incorrect")
    
    