import math

def escolhas(n, k):
    resultado, k = 1, float(min(k,n-k))

    while k > 0:
        resultado *= n/k
        k -= 1
        n -= 1

    resultado = math.ceil(resultado)

    return resultado

