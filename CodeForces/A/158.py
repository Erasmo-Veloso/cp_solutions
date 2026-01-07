#https://codeforces.com/problemset/problem/158/A

n , k = map(int, input().split())

arrin = input().split()
arrin = [int(a) for a in arrin]

k_place = arrin[k-1]

nextRound = 0 

for element in arrin:
    if element >= k_place and element != 0:
        nextRound += 1



print(nextRound)