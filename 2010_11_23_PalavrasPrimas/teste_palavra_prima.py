import unittest

from palavra_prima import funcao_palavra_prima, _IS_NOT_PRIME, _IS_PRIME, numero_eh_primo

class TestePalavraPrima(unittest.TestCase):
    def teste_um_caracter_primo(self):
        self.assertEqual(funcao_palavra_prima('a'), _IS_PRIME)
        
    def teste_um_caracter_nao_primo(self):
        self.assertEqual(funcao_palavra_prima('d'), _IS_NOT_PRIME)    
        self.assertEqual(funcao_palavra_prima('f'), _IS_NOT_PRIME)

    def teste_dois_caracteres_primo(self):
        " Palavras com dois caracteres primas. "
        self.assertEqual(funcao_palavra_prima('ab'), _IS_PRIME)
        
    def teste_tres_caracteres_primo(self):
        self.assertEqual(funcao_palavra_prima('aaa'), _IS_PRIME)
        
    def teste_palavras_primas(self):
        self.assertEqual(funcao_palavra_prima('UFRN'), _IS_PRIME)
        
    def teste_palavras_nao_primas(self):
        self.assertEqual(funcao_palavra_prima('contest'), _IS_NOT_PRIME)
        self.assertEqual(funcao_palavra_prima('AcM'), _IS_NOT_PRIME)

    def teste_eh_primo(self):
        self.assertEqual(numero_eh_primo(2), True)
        self.assertEqual(numero_eh_primo(3), True)
        self.assertEqual(numero_eh_primo(101), True)
    
    def teste_nao_eh_primo(self):
        self.assertEqual(numero_eh_primo(4), False)
        self.assertEqual(numero_eh_primo(9), False)
        self.assertEqual(numero_eh_primo(39), False)
        self.assertEqual(numero_eh_primo(1000), False)
        

if __name__ == '__main__':
    unittest.main()
