# -*- coding: utf-8 -*-

cases = int(input())

for _ in range(cases):
    line = input()
    mid = len(line)//2
    part_one = line[:mid][:-1]
    part_two = line[(mid+1):][:-1]
    
    result = ""
    
    for letter in part_one:
        result += letter
    for letter in part_two:
        result += letter
        
    print(result)
    