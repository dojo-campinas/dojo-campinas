import unittest
from troco import devolve_troco
class TrocoTestCase(unittest.TestCase):

    def teste_valor_total_igual_valor_dado(self):
        self.assertEqual(devolve_troco(10.0, 10.0), {})

    def teste_troco_de_um_centavo(self):
        self.assertEqual(devolve_troco(2, 1.99), {'0.01': 1})

    def teste_troco_de_cinco_centavos(self):
        self.assertEqual(devolve_troco(5.00, 4.95), {'0.05': 1})

    def teste_troco_de_seis_centavos(self):
        self.assertEqual(devolve_troco(7.00, 6.94), {'0.01': 1, '0.05': 1})

    def teste_troco_de_nove_centavos(self):
        self.assertEqual(devolve_troco(5.00, 4.91), {'0.01': 4, '0.05': 1})

    def teste_troco_de_dez_centavos(self):
        self.assertEqual(devolve_troco(10.00, 9.90), {'0.10': 1})

    def teste_troco_de_onze_centavos(self):
        self.assertEqual(devolve_troco(10.00, 9.89), {'0.10': 1, '0.01': 1})	

    def teste_troco_de_cinquenta_centavos(self):
        self.assertEqual(devolve_troco(15.00, 14.50), {'0.50': 1})

    def teste_troco_de_sessenta_e_seis_centavos(self):
        self.assertEqual(devolve_troco(3.00, 2.34), {'0.50': 1, '0.10': 1, '0.05': 1, '0.01': 1})

    def teste_troco_de_um_real(self):
        self.assertEqual(devolve_troco(3.34, 2.34), {'1.00': 1})


    def teste_troco_de_cento_e_sessenta_e_seis_reais_e_sete_centavos(self):
        self.assertEqual(devolve_troco(500, 333.93), {'100.00':1, 
						      '50.00':1,
						      '10.00':1,
                                                      '5.00':1,
                                                      '1.00':1,
                                                      '0.05':1,
                                                      '0.01':2})

if __name__ == "__main__":
    unittest.main()
