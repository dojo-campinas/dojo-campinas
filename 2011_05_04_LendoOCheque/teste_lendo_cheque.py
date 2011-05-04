# -*- coding: utf-8 -*-
import unittest
from lendo_cheque import leia_cheque

class TesteLendoChequeTestCase(unittest.TestCase):

    def test_entra_um_sai_1(self):
        self.assertEqual(leia_cheque('um real'), 1.00)
        
    def test_entra_dois_sai_2(self):
        self.assertEqual(leia_cheque('dois reais'), 2.00)
      
    def test_entra_tres_sai_3(self):
        self.assertEqual(leia_cheque('tres reais'), 3.00)
    
    def test_quatro_a_nove(self):
        self.assertEqual(leia_cheque('quatro reais'), 4.00)
        self.assertEqual(leia_cheque('cinco reais'), 5.00)
        self.assertEqual(leia_cheque('seis reais'), 6.00)
        self.assertEqual(leia_cheque('sete reais'), 7.00)
        self.assertEqual(leia_cheque('oito reais'), 8.00)
        self.assertEqual(leia_cheque('nove reais'), 9.00)
    
    def test_dez_a_15(self):
        self.assertEqual(leia_cheque('dez reais'),10.00)
        self.assertEqual(leia_cheque('onze reais'),11.00)
        self.assertEqual(leia_cheque('doze reais'),12.00)
        self.assertEqual(leia_cheque('treze reais'),13.00)
        self.assertEqual(leia_cheque('quatorze reais'),14.00)
        self.assertEqual(leia_cheque('quinze reais'),15.00)
        
    
    def test_entra_vinte_sai_20(self):
        self.assertEqual(leia_cheque('vinte reais'), 20.00)
    
    def test_entra_vinteUm_sai21(self):
        self.assertEqual(leia_cheque('vinte e um reais'), 21.00)

    def test_multiplos_10(self):
        self.assertEqual(leia_cheque('trinta reais'), 30.00)
        self.assertEqual(leia_cheque('quarenta reais'), 40.0)
        self.assertEqual(leia_cheque('cinquenta reais'), 50.0)
        self.assertEqual(leia_cheque('sessenta reais'), 60.0)
        self.assertEqual(leia_cheque('setenta reais'), 70.0)
        self.assertEqual(leia_cheque('oitenta reais'), 80.0)
        self.assertEqual(leia_cheque('noventa reais'), 90.0)
        
    def test_entra_trinta_e_um_sai_31(self):
        self.assertEqual(leia_cheque('trinta e um reais'), 31.00)
        
    def test_entra_sessenta_e_sete_sai_67(self):
        self.assertEqual(leia_cheque('sessenta e sete reais'), 67.00)
        
    def test_entra_noventa_e_nove_sai_99(self):
        self.assertEqual(leia_cheque('noventa e nove reais'), 99.00)
        
    def test_entra_um_centavo_sai_001(self):
        self.assertEqual(leia_cheque('um centavo'),0.01)
    
    def test_entra_dois_centavos_sai_002(self):
        self.assertEqual(leia_cheque('dois centavos'),0.02)
    
    def test_entra_dois_centavos_sai_010(self):
        self.assertEqual(leia_cheque('dez centavos'),0.10)
    
    def test_entra_dois_centavos_sai_099(self):
        self.assertEqual(leia_cheque('noventa e nove centavos'),0.99)

    def test_entra_dois_centavos_sai_101(self):
        self.assertEqual(leia_cheque('um real e um centavo'),1.01)

unittest.main()
