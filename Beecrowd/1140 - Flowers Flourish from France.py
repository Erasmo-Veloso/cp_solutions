# -*- coding: utf-8 -*-

while True:
    line = input().split()
    if line[0] == "*":
        break
    initial_letters = [ word[0].lower() for word in line ]
    c = 0
    for letter in initial_letters:
        if initial_letters[0] == letter:
            c+=1
    if c == len(initial_letters):
        print("Y")
    else:
        print("N")
    