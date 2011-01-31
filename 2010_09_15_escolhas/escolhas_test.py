import unittest

from escolhas import escolhas

class EscolhaTestCase(unittest.TestCase):
    def test_k_igual_n(self):
        "Testando k igual a n deve retornar 1"

        self.assertEquals(escolhas(1,1), 1)

    def test_k_igual_zero(self):
        "Testando k igual a zero deve retornar 1"

        self.assertEquals(escolhas(1,0), 1)

    def test_k_igual_um(self):
        "Testando k igual a um deve retornar n"

        for n in range(1,10):
            self.assertEquals(escolhas(n,1), n)

    def test_k_igual_dois(self):
        "Testando k igual a dois deve retornar n*(n-1)/2"

        for n in range(2,10):
            self.assertEquals(escolhas(n,2), n*(n-1)/2)

    def test_k_igual_n_menos_k(self):
        "Testando se (n,k) igual a (n,n-k)"

        self.assertEquals(escolhas(3,2), escolhas(3,1))
        self.assertEquals(escolhas(4,1), escolhas(4,3))
        self.assertEquals(escolhas(5,2), escolhas(5,3))
        self.assertEquals(escolhas(7,3), escolhas(7,4))

    def test_k_igual_tres(self):
        "Testando k igual a 3"

        for n in range(3,10):
            self.assertEquals(escolhas(n,3), n*(n-1)*(n-2)/6)

    def test_k_igual_quatro(self):
        "Testando k igual a 4"

        self.assertEquals(escolhas(6,4), 15)

    def test_n_muito_grande(self):
        "Testando n muito grande para ver se o resultado estoura um byte"

        self.assertEquals(escolhas(2**10,0),1)
        self.assertEquals(escolhas(2**10,2**10),1)

if __name__ == "__main__":
    unittest.main()
