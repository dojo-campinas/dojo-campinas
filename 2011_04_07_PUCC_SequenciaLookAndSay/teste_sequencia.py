# -*- coding: utf-8 -*-
import unittest
from sequencia import proximo_item


class SequenciaLookAndSayTestCase(unittest.TestCase):
    
    def test_entra_n_sai_1_n(self):
        for n in range(1, 10):
            self.assertEquals(proximo_item(n), int("1" + str(n)))

    def test_entra_1_1_sai_2_1(self):
        self.assertEquals(proximo_item(11), 21)

    def test_entra_1_n_sai_1_1_1_n(self):
        for n in range(2,10):
            item_anterior = int("1" + str(n))
            self.assertEquals(proximo_item(item_anterior), 
                              int("111" + str(n)))
    def test_entra_1_1_1_sai_3_1(self):
        self.assertEquals(proximo_item(111), 31)
        
    def test_entra_1_1_n_sai_2_1_n(self):
        for  n in range (2,10):
            item = int("21"+str(n))
            self.assertEquals(proximo_item(item),int("21" + str(n)))
    
if __name__ == '__main__':
    unittest.main()

