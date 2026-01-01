import sys
input = sys.stdin.readline
cidade = 0

while True:
    N = int(input())
    if N == 0:
        break

    cidade += 1
    consumo = {}
    total_pessoas = 0
    total_consumo = 0

    for _ in range(N):
        X, Y = map(int, input().split())
        c = Y // X
        consumo[c] = consumo.get(c, 0) + X
        total_pessoas += X
        total_consumo += Y

    if cidade > 1:
        print()

    print(f"Cidade# {cidade}:")

    for c in sorted(consumo):
        print(f"{consumo[c]}-{c}", end=" ")
    print()

    media = total_consumo / total_pessoas
    media = int(media * 100) / 100

    print(f"Consumo medio: {media:.2f} m3.")
