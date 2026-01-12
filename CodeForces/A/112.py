#https://codeforces.com/problemset/problem/112/A

def main(s1, s2)->int:
    if s1.lower() == s2.lower(): return 0

    for i, s in enumerate(s1):
        if(s.lower() == s2[i].lower()):
            continue
        else:
            if(s.lower() > s2[i].lower()):
                return 1
            else:
                return -1

s1 = input()
s2 = input()

print(main(s1,s2))