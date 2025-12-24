# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run iw

c = 0
while True:
    N = int(input())
    if (N == 0 ): 
        break
    if( c!=0):
        print()
    words = []
    biggest_len = 0
    for i in range(N):
        word = input()
        words.append(word)
        if (len(word) > biggest_len):
            biggest_len = len(word)
    
    for word in words:
        n_space = biggest_len - len(word)
        initial = n_space*" "
        print(f'{initial}{word}')
    c+=1
