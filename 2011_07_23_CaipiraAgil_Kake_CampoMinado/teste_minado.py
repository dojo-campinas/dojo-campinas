# -*- coding: utf-8 -*-
import unittest
from minado import retorna_mapa

class CampoMinadoTestCase(unittest.TestCase):
    
    def test_recebe_mapa_2x2_vazio(self):
        mapa = [['.','.'],['.','.'],]
        self.assertEqual(retorna_mapa(mapa), [['0','0'],['0','0'],])

#    def test_recebe_mapa_2x2_com_1_mina(self):
#        mapa = [['*','.'],['.','.'],]
#        self.assertEqual(retorna_mapa(mapa), [['*','1'],['1','1'],])

#    def test_recebe_mapa_2x2_com_2_minas_diagonal(self):
#        mapa = [['*','.'],['.','*'],]
#        self.assertEqual(retorna_mapa(mapa), [['*','2'],['2','*'],])

    def test_recebe_mapa_3x3_com_1_mina_no_meio(self):
        mapa = [['.', '.', '.'], ['.', '*', '.'], ['.','.', '.'],]
        self.assertEqual(retorna_mapa(mapa), [['1', '1', '1'], ['1', '*', '1'], ['1','1', '1'],])


if __name__ == '__main__':
    unittest.main()
