# coding: utf-8
import unittest

import relogio

class TesteRelogio(unittest.TestCase):

    def setUp (self):
        self.rel = relogio.Relogio()

    def test_classe(self):
        self.assertTrue(isinstance(self.rel, relogio.Relogio))
        
    def test_relogio_sem_ponteiro(self):
        self.assertEqual(self.rel._blank(), bytearray('oooooooooooo'))

    def test_relogio_data(self):
        self.assertTrue(hasattr(self.rel, "data"))
    
    def test_data_eh_relogio_vazio (self):
        self.assertTrue(isinstance(self.rel.data, bytearray))
        self.assertEqual(len(self.rel.data), 12)
    
    def test_data_eh_relogio_sem_ponteiro(self):
        self.assertEqual(self.rel.data, bytearray('oooooooooooo'))
    
    def test_criar_relogio_com_horario_funciona(self):
        try:
            rel = relogio.Relogio("21:00")
        except TypeError:
            self.fail('Não criou relogio com horario')
            
    def test_existe_ponteiro_de_hora(self):
        rel = relogio.Relogio("21:00")
        self.assertTrue("h" in rel.data)

    def test_existe_ponteiro_de_minuto(self):
        rel = relogio.Relogio("21:00")
        self.assertTrue("m" in rel.data)
        
    def test_hora_no_lugar_certo(self):
        rel = relogio.Relogio("1:00")
        self.assertEqual(rel.data[1], ord("h"))
        
    def test_hora_no_lugar_certo2(self):
        rel = relogio.Relogio("2:00")
        self.assertEqual(rel.data[2], ord("h"))
    
    def test_tem_no_maximo_1_h(self):
        rel = relogio.Relogio("4:00")
        self.assertEqual(rel.data.count("h"), 1)
    
if __name__ == '__main__':
    unittest.main()
