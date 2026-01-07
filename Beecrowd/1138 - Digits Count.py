# -*- coding: utf-8 -*-

while True:
    start, end = map(int, input().split())
    if start == 0 and end == 0:
        break
    dic = {}
    while start <= end:
        nums = str(start)
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        start+=1
    result = ""
    for i in range(10):
        result += str(dic.get(str(i),0))
        if i != 9:
            result += " "
    print(result)