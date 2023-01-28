def knapsack(precio, pesos, peso_maximo):
    n = len(precio)
    mochila = [[0 for x in range(peso_maximo + 1)] for y in range(n + 1)]
    for i in range(1, n+1):
        for w in range(1, peso_maximo+1):
            if pesos[i-1] <= w:
                mochila[i][w] = max(precio[i-1] + mochila[i-1][w-pesos[i-1]], mochila[i-1][w])
            else:
                mochila[i][w] = mochila[i-1][w]
    return mochila[n][peso_maximo]