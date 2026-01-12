#https://codeforces.com/problemset/problem/236/A

word = input().strip()

word = "".join(set(word))

if word.__len__() % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
