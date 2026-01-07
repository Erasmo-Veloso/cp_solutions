
values = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10,5, 1]
Map_values = {}

N = int(round(float(input())*100))

for value in values:
    V = N // value
    N = N%value
   
    Map_values[value] = V

print("NOTAS:")
for value in Map_values:
    if value > 100:
        print(f'{(Map_values[value]):.0f} nota(s) de R$ {(value/100):.2f}')

print("MOEDAS:")
for value in Map_values:
    if value <= 100:
        print(f'{(Map_values[value]):.0f} moeda(s) de R$ {(value/100):.2f}')
