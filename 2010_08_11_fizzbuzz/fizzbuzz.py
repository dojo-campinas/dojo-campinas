import unittest

def fizzbuzz(numero):
    if numero == 0:
        return str(0)
    elif not numero % 15:
        return "fizzbuzz"
    elif not numero % 5:
        return "buzz"
    elif not numero % 3:
        return "fizz"
    else:
        return str(numero)

class FizzBuzzTest(unittest.TestCase):
    def testaSeNumeroRetornoNumero(self):
        self.assertEquals(fizzbuzz(4), "4")
        
    def testaSeMultiploTresRetornoFizz(self):
        self.assertEquals(fizzbuzz(3), "fizz")
        self.assertEquals(fizzbuzz(9), "fizz")
    
    def testaSeMultiploCincoRetornoBuzz(self):
        self.assertEquals(fizzbuzz(5), "buzz")
    
    def testaSeMultiploTresECincoRetornoFizzBuzz(self):
        self.assertEquals(fizzbuzz(15), "fizzbuzz")
        
    def testaSeZeroRetornoZero(self):
        self.assertEquals(fizzbuzz(0), "0")
    
if __name__ == "__main__":
    unittest.main()
