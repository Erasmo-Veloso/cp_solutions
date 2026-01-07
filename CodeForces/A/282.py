#https://codeforces.com/problemset/problem/282/A

n = int(input())
x = 0
for _ in range(n):
    word = input()
    if "+" in word:
        x+=1
    else:
        x -= 1
        
print(x)