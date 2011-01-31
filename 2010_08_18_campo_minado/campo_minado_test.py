import unittest
from campo_minado import campo_minado


class CampoMinadoTestCase(unittest.TestCase):
    def test_mapa_1_por_1(self):
        self.assertEquals(campo_minado("*"), "*") 
        self.assertEquals(campo_minado("_"), "0")

    def test_mapa_1_por_2(self):
        self.assertEquals(campo_minado("**"), "**") 
        self.assertEquals(campo_minado("*_"), "*1")
        self.assertEquals(campo_minado("_*"), "1*")
        self.assertEquals(campo_minado("__"), "00")

    def test_mapa_2_por_2(self):
        self.assertEquals(campo_minado("**\n**"), "**\n**")
        self.assertEquals(campo_minado("_*\n**"), "3*\n**")
        self.assertEquals(campo_minado("_*\n*_"), "2*\n*2")
        
    def test_mapa_3_por_3(self):
        self.assertEquals(campo_minado("***\n***\n***"), "***\n***\n***")
        self.assertEquals(campo_minado("*__\n___\n___"), "*10\n110\n000")
        
    def test_mapa_apresentacao(self):
        self.assertEquals(campo_minado("__*_\n" \
                                       "____\n" \
                                       "_*__\n" \
                                       "____"),
                                       "01*1\n" \
                                       "1221\n" \
                                       "1*10\n" \
                                       "1110")
   

if __name__ == "__main__":
    unittest.main()
