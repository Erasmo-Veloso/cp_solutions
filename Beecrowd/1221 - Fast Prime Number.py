N = int(input())

for _ in range(N):
    number = int(input())
    c = 0
    isPrime = False
    for i in range(number):
        if c > 2:
            isPrime = True
            break
        x = i+1
        if number%x == 0:
            c+=1
    print("Not Prime" if isPrime else "Prime")