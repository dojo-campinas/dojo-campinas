# coding: utf-8 

from cheque import extenso
from unittest import TestCase, main

class TestesExtenso(TestCase):
    def teste_um_por_extenso(self):
        self.assertEquals(extenso(1), "um real")
    def teste_cinco_por_extenso(self):
        self.assertEquals(extenso(5), "cinco reais")
    def teste_dez_por_extenso(self):
        self.assertEquals(extenso(10), "dez reais")
    def teste_um_centavo(self):
        self.assertEquals(extenso(0.01), "um centavo")
    def teste_dez_centavos(self):
        self.assertEquals(extenso(0.10), "dez centavos")
    def teste_cinquenta_centavos(self):
        self.assertEquals(extenso(0.50), "cinquenta centavos")
    def teste_um_real_e_um_centavo(self):
        self.assertEquals(extenso(1.01), "um real e um centavo")
    def teste_um_real_e_dez_centavos(self):
        self.assertEquals(extenso(1.10), "um real e dez centavos")
    def teste_vinte_reais_e_vinte_centavos(self):
        self.assertEquals(extenso(20.20), "vinte reais e vinte centavos")
    def teste_vinte_e_um_reais_e_cinquenta_e_um_centavos(self):
        self.assertEquals(extenso(21.51), "vinte e um reais e cinquenta e um centavos")
    def teste_vinte_e_tres_reais(self):
        self.assertEquals(extenso(23), "vinte e três reais")
    def teste_12_reais_e_dezenove_centavos(self):
        self.assertEquals(extenso(12.19), "doze reais e dezenove centavos")
    def teste_quarenta_reais_e_quinze_centavos(self):
        self.assertEquals(extenso(40.15), "quarenta reais e quinze centavos")
    def teste_noventa_e_nove_reais_e_noventa_e_nove_centavos(self):
        self.assertEquals(extenso(99.99), "noventa e nove reais e noventa e nove centavos")
    def teste_zero_zero(self):
        self.assertRaises(ValueError,extenso,0.00)
    def teste_valor_negativo(self):
        self.assertRaises(ValueError,extenso,-42)
    def teste_cem_reais(self):
        self.assertEquals(extenso(100), "cem reais")
    def teste_cento_e_um(self):
        self.assertEquals(extenso(101), "cento e um reais")
    def teste_novecentos_e_noventa_e_nove_e_noventa_e_nove(self):
        self.assertEquals(extenso(999.99), "novecentos e noventa e nove reais e noventa e nove centavos")
if __name__ == "__main__":
    main()
