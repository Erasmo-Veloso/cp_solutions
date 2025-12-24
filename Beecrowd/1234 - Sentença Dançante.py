# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import sys
for linha in sys.stdin:
    linha = linha.rstrip()
    c = 0
    s = ""
    for letter in linha:
        if (c % 2 == 0):
            s+=letter.upper()
        else:
            s+=letter.lower()
            
        if letter.isalpha():
            c+=1
        else:
            continue
    print(s)