while True:
    N = int(input().strip())

    if N == 0:
        break
    else:
        valores = [i+1 for i in range(N)]
        cartas = sorted(valores, reverse=True)
        discartadas = []

        while len(cartas) >= 2:
            discartada = cartas.pop()
            ultima = cartas.pop()
            cartas.insert(0, ultima)
            discartadas.append(discartada)
        

        response = "".join([f'{discartada}, 'if index < len(discartadas) -1 else f'{discartada}' for index, discartada in enumerate(discartadas)])
        print("Discarded cards: ", response)
        print("Remaining card: ", cartas[0])
        
       

        

