import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    Word = input().strip()
    fWord = ''
    SWord = ''
    lWord = ''
    
    for letter in Word:
        if letter.isalpha():
            letter = chr(ord(letter) + 3)
            fWord += letter
        else:
            fWord += letter
    
    SWord = fWord[::-1]
    metade = len(SWord) // 2
    
    for i, letter in enumerate(SWord):
        if i >= metade:
            letter = chr(ord(letter) - 1)
            lWord += letter
        else:
            lWord += letter
    print(lWord)
    