import unittest

from harry import livraria, CUSTO_UNITARIO, DESCONTO

class HarryTestCase(unittest.TestCase):
    def test_nenhuma_compra_nao_pago_nada(self):
        self.assertEquals(livraria("0 0 0 0 0 0 0"), 0.00)
        
    def test_um_titulo_qualquer_custa_CUSTO(self):
        self.assertEquals(livraria("1 0 0 0 0 0 0"), CUSTO_UNITARIO)
    
    def test_n_titulos_iguais_dah_n_vezes_CUSTO(self):
        self.assertEquals(livraria("5 0 0 0 0 0 0"), 5*CUSTO_UNITARIO)
        
    def test_2_titulos_diferentes_dah_desconto_aos_pares(self):
        self.assertEquals(livraria("1 1 0 0 0 0 0"), CUSTO_UNITARIO*DESCONTO[2]*2)
        self.assertEquals(livraria("2 1 0 0 0 0 0"), CUSTO_UNITARIO*DESCONTO[2]*2+CUSTO_UNITARIO)
        self.assertEquals(livraria("2 2 0 0 0 0 0"), CUSTO_UNITARIO*DESCONTO[2]*4)
        self.assertEquals(livraria("0 5 0 0 3 0 0"), CUSTO_UNITARIO*DESCONTO[2]*6 + 2*CUSTO_UNITARIO)
    
    def test_3_titulos_diferentes_dah_desconto_aos_trios(self):
        self.assertEquals(livraria("1 1 1 0 0 0 0"), CUSTO_UNITARIO*DESCONTO[3]*3)
        self.assertEquals(livraria("2 1 1 0 0 0 0"), CUSTO_UNITARIO*DESCONTO[3]*3 + CUSTO_UNITARIO)
    
        
if __name__ == "__main__":
    unittest.main()
