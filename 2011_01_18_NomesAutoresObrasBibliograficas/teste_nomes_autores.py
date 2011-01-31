import unittest
from nomes_autores import converte

class Teste_Nomes (unittest.TestCase):

    def teste_nome_simples (self):
        self.assertEqual(converte("Joao"), "JOAO")
        self.assertEqual(converte("Guimaraes"), "GUIMARAES")
        
    def teste_nome_com_dois (self):
        self.assertEqual(converte("Joao Silva"), "SILVA, Joao")
       
    def teste_nome_composto_com_parentesco_no_fim(self):
        self.assertEqual(converte("Joao Silva Filho"), "SILVA FILHO, Joao")
        self.assertEqual(converte("Joao Silva Neto"), "SILVA NETO, Joao")
        self.assertEqual(converte("Joao Silva Sobrinho"), "SILVA SOBRINHO, Joao")
        self.assertEqual(converte("Joao Silva Junior"), "SILVA JUNIOR, Joao")
        self.assertEqual(converte("Maria Silva Filha"), "SILVA FILHA, Maria")
        self.assertEqual(converte("Maria Silva Neta"), "SILVA NETA, Maria")
        self.assertEqual(converte("Maria Silva Sobrinha"), "SILVA SOBRINHA, Maria")


    def teste_nome_composto_sem_parentesco(self):
        self.assertEqual(converte("Joao Silva Santos"), "SANTOS, Joao Silva")

if __name__ == "__main__":
  unittest.main()
