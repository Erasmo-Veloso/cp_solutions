c_positives = 0
total_positives = 0

for _ in range(6):
    number = float(input())
    if number > 0:
        c_positives += 1
        total_positives += number
        
print(f'{c_positives} valores positivos\n{(total_positives/c_positives):.1f}')
