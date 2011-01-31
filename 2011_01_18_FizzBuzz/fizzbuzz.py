
def fizzbuzz(limite):
    retornar = []
    for numero in xrange(1,limite+1):
        if numero % 3 == 0 and numero % 5 == 0:
            retornar.append("FizzBuzz")
        elif numero % 3 == 0:
            retornar.append("Fizz")
        elif numero % 5 == 0:
            retornar.append("Buzz")
        else:
            retornar.append(numero)
    return retornar

