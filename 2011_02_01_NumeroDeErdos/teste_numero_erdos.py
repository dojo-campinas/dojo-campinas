#!/usr/bin/env python
#! *-* coding: utf-8 *-*

import unittest
from numero_erdos import retorna_erdos


class TesteNumeroErdos(unittest.TestCase):
    def teste_erdos_eh_zero(self):
        entrada = [ ('Publicação 1', 'Erdos'), ]
        self.assertEquals(retorna_erdos(entrada), {'Erdos': 0})

    def teste_um_autor_junto_com_erdos(self):
        entrada = [ ('Publicação 1', 'Erdos', 'Autor 1'), ]
        self.assertEquals(retorna_erdos(entrada), {'Erdos': 0, 'Autor 1': 1})
        entrada = [ ('Publicação 1', 'Erdos', 'Autor 2'), ]
        self.assertEquals(retorna_erdos(entrada), {'Erdos': 0, 'Autor 2': 1})
    def teste_varios_autores_com_erdos(self):
        entrada = [ ("pub 3", "Erdos", "Autor 1", "Autor 2")]
        self.assertEquals(retorna_erdos(entrada),{'Erdos':0, 'Autor 1':1,'Autor 2':1})

    def teste_duas_publicacoes_com_erdos(self):
        entrada = [ ("pub 4", "Erdos", "Autor 1"),("pub 5","Erdos","Autor 2")]
        self.assertEquals(retorna_erdos(entrada),{'Erdos':0,'Autor 1':1, 'Autor 2':1})

    def teste_duas_publicacoes_com_uma_sem_erdos(self):
        entrada = [ ("pub 1", "Erdos", "Autor 1"),
                    ("pub 2", "Autor 1", "Autor 2") ]
        self.assertEquals(retorna_erdos(entrada), {'Erdos': 0, 'Autor 1': 1, 'Autor 2': 2})

    def teste_duas_publicacoes_com_erdos2(self):
        entrada = [ ("pub 1", "Erdos", "Autor 1"),
                    ("pub 2", "Autor 1", "Autor 3","Erdos") ]
        self.assertEquals(retorna_erdos(entrada), {'Erdos': 0, 'Autor 1': 1, 'Autor 3': 1})

    def teste_autor_com_erdos_infinito(self):
        entrada = [ ("Publicação 1", "Erdos", "Autor 1"),
                    ("Publicação 2", "Autor 3"), ]
        self.assertEquals(retorna_erdos(entrada), {'Erdos': 0, 'Autor 1': 1, 'Autor 3': None})

    def teste_um_montao_de_publicacoes(self):
        entrada = [ ("", "Erdos", "Autor 1"),
                    ("", "Autor 1", "Autor 2"),
                    ("", "Autor 2", "Autor 3"),
                    ("", "Autor 3", "Autor 4"),
                    ("", "Autor 4", "Autor 5"),
                    ("", "Autor 5", "Autor 6"),
                    ("", "Autor 6", "Autor 7"),
                    ("", "Autor 7", "Autor 8"),
                    ("", "Autor 8", "Autor 9"),
                    ("", "Autor 9", "Autor 10"),
                    ("", "Autor 10", "Autor 11"),
                    ("", "Autor 11", "Autor 12"),
                    ("", "Autor 12", "Autor 13"),
                    ("", "Autor 13", "Autor 14"), ]
        saida = {"Autor %d"%i:i for i in range(1,15)}
        saida["Erdos"] = 0
        self.assertEquals(retorna_erdos(entrada), saida)
        entrada.append(("", "Erdos") + tuple("Autor %d" %i for i in xrange(1,15 )))
        for autor in saida:
            if autor != "Erdos":
                saida[autor] = 1
        self.assertEquals(retorna_erdos(entrada), saida)
        entrada.append(("", "bla", "Autor 1"))
        saida["bla"] = 2
        self.assertEquals(retorna_erdos(entrada), saida)

if __name__ == "__main__":
    unittest.main()
