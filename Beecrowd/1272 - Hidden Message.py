# -*- coding: utf-8 -*-

i = int(input())

for _ in range(i):
    st = input().split(" ")
    st_final = ""
    
    
    for letter in st:
        if letter == "":
            continue
        if letter[0].isalpha():
            st_final+=letter[0]
            
    print(st_final)