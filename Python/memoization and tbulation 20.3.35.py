def fibo(n):
    fiboTable = [0] * (n + 1)
    fiboTable[0] = 0
    fiboTable[1] = 1
    index = 2
    while index <= n:
        fiboTable[index] = fiboTable[index - 1] + fiboTable[index - 2]
        index += 1
    return fiboTable[n]

print( fibo(3000) )