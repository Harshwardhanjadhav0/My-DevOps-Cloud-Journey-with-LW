InfoMem = {0: 0, 1: 1} # dictionary

def fibo(n):
    if n < 0:
        return"not supported"
    elif n in InfoMem:
        return InfoMem[n]
    else: 
        output = fibo(n - 1) + fibo(n - 2)
        InfoMem[n] = output
        print(InfoMem)
        return InfoMem[n]

print (fibo(15))