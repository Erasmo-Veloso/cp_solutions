#https://codeforces.com/problemset/problem/231/A

n = int(input())
c = 0
for _ in range(n):
    n1, n2, n3 = map(int, input().split())
    if(n1+n2+n3) >= 2:
        c+=1
print(c)
