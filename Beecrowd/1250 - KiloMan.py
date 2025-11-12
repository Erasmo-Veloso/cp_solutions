# -*- coding: utf-8 -*-

N = int(input())



for i in range(N):
    heights = []
    position = []
    Shots = int(input())
    heights = input().split(" ")
    position = str(input())
    position = list(position)
    shoted = 0
    for i in range(Shots):
        if position[i] == "J" and int(heights[i]) > 2:
            shoted+=1
        elif position[i] == "S" and int(heights[i]) <= 2:
            shoted+=1
    print(shoted)
            
            
    
    