# -*- coding: utf-8 -*-
import unittest

def imprime():
    for i in range(1,101):
        print fizzbuzz(i)

def fizzbuzz(n):
    return 'fizzbuzz' if n % 3 == 0 and n % 5 == 0 else 'fizz' if n % 3 == 0 else 'buzz' if n % 5 == 0 else n

def fizzbuzz_old(n):
    retorno = n
    
    if divisivel_por_tres(n) and divisivel_por_cinco(n):
        retorno = 'fizzbuzz'
    elif divisivel_por_tres(n):
        retorno = 'fizz'
    elif divisivel_por_cinco(n):
        retorno = 'buzz'
        
    return retorno


def divisivel_por_tres(n):
    return n % 3 == 0
        
def divisivel_por_cinco(n):
    return n % 5 == 0

class FizzBuzzTestCase(unittest.TestCase):
    
    def test_entra_um_sai_um(self):
        self.assertEqual(fizzbuzz(1), 1)
    
    def test_entra_dois_sai_dois(self):
        self.assertEqual(fizzbuzz(2), 2)
        
    def test_entra_tres_sai_fizz(self):
        self.assertEqual(fizzbuzz(3),'fizz')
        
    def test_entra_cinco_sai_buzz(self):
        self.assertEqual(fizzbuzz(5), 'buzz')
        
    def teste_entra_seis_sai_fizz(self):
        self.assertEqual(fizzbuzz(6), 'fizz')
        
    def teste_divisivel_por_tres(self):
        self.assertEqual(divisivel_por_tres(3), True)
        
    def test_nao_divisivel_por_tres(self):
        self.assertEqual(divisivel_por_tres(5),False)
    
    def test_divisivel_por_cinco(self):
        self.assertEqual(divisivel_por_cinco(5), True)
        
    def test_nao_divisivel_por_cinco(self):
        self.assertEqual(divisivel_por_cinco(6), False)
        
    def test_entra_dez_sai_buzz(self):
        self.assertEqual(fizzbuzz(10), 'buzz')
        
    def test_entra_quinze_sai_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')
        
if __name__ == '__main__':
    unittest.main()
    #imprime()
