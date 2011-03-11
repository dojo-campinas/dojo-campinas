# -*- coding: utf-8 -*-
import unittest
import cinzas


class TestCinza(unittest.TestCase):
    def teste_mapa_eh_criado(self):
        try:
            mapa = cinzas.Mapa(".")
        except Exception, e:
            self.fail("Erro: %s" % e)

    def teste_mapa_uma_linha_uma_coluna(self):
        mapa = cinzas.Mapa(".")
        self.assertEqual(mapa.altura, 1)
        self.assertEqual(mapa.largura, 1)

    def teste_mapa_um_por_dois(self):
        mapa = cinzas.Mapa("..")
        self.assertEqual(mapa.altura, 1)
        self.assertEqual(mapa.largura, 2)
        
    def teste_mapa_dois_por_dois(self):
        mapa = cinzas.Mapa("..\n..")
        self.assertEqual(mapa.altura, 2)
        self.assertEqual(mapa.largura, 2)

    def teste_mapa_n_por_m(self):
        for n in range(2,10):
            for m in range(2,10):
                conteudo = ("." * n + "\n") * m
                mapa = cinzas.Mapa(conteudo)
                self.assertEqual(mapa.largura, n)
                self.assertEqual(mapa.altura, m)

    def teste_mapa_contem_aeroportos(self):
        mapa = cinzas.Mapa("A")
        self.assertEqual(mapa.conta_aeroportos(), 1)
        mapa = cinzas.Mapa("AA")
        self.assertEqual(mapa.conta_aeroportos(), 2)
        mapa = cinzas.Mapa("AA\nAA")
        self.assertEqual(mapa.conta_aeroportos(), 4)

    def teste_obtem_ponto_no_mapa(self):
        mapa = cinzas.Mapa(".")
        self.assertEqual(mapa[0, 0], ".")

        mapa = cinzas.Mapa("A")
        self.assertEqual(mapa[0, 0], "A")
        
        mapa = cinzas.Mapa(".A.\n"
                           "*.A")
        self.assertEqual(mapa[0,0],".")
        self.assertEqual(mapa[0,1],"*")
        self.assertEqual(mapa[1,0],"A")
        self.assertEqual(mapa[1,1],".")
        self.assertEqual(mapa[2,0],".")
        self.assertEqual(mapa[2,1],"A")
        
    def teste_set_item(self):
        mapa = cinzas.Mapa(".")
        self.assertEqual(mapa[0,0], ".")
        mapa[0,0] = "*"
        self.assertEqual(mapa[0,0], "*")

        mapa = cinzas.Mapa(".A\n"
                           "*.")
        self.assertEqual(mapa[1,1], ".")
        mapa[1,1] = "*"
        self.assertEqual(mapa[1,1], "*")

    def teste_passa_dia(self):
        mapa = cinzas.Mapa("*A")
        mapa.passa_dia()
        self.assertEqual(mapa.conta_aeroportos(), 0)

        mapa = cinzas.Mapa("A*")
        mapa.passa_dia()
        self.assertEqual(mapa.conta_aeroportos(), 0)

        mapa = cinzas.Mapa("A*.\n"
                           ".A.")
        mapa.passa_dia()
        self.assertEqual(mapa.conta_aeroportos(), 0)
    
    def teste_passa_dois_dias(self):
        mapa = cinzas.Mapa("*AA")
        #print "\n", mapa
        mapa.passa_dia()
        #print mapa
        self.assertEqual(mapa.conta_aeroportos(), 1)
        mapa.passa_dia()
        #print mapa
        self.assertEqual(mapa.conta_aeroportos(), 0)

    def teste_conta_some_primeiro_aeroporto(self):
        mapa = cinzas.Mapa("""
A...
....
*...
        """)
        self.assertEqual(mapa.some_primeiro_aeroporto(), 2)

    def teste_some_dois_aeroportos_em_um_dia(self):
        mapa = cinzas.Mapa("""
A*..
....
*A..
        """)
        self.assertEqual(mapa.some_primeiro_aeroporto(), 1)

    def teste_mapa_sem_aeroporto(self):
        mapa = cinzas.Mapa("""
.*..
....
*...
        """)
        self.assertEqual(mapa.some_primeiro_aeroporto(), None)

    def teste_conta_some_todos_aeroportos(self):
        mapa = cinzas.Mapa("""
.A..
....
*.A.
        """)
        self.assertEqual(mapa.some_primeiro_aeroporto(), 2)
        self.assertEqual(mapa.some_todos_aeroportos(), 3)
        
    def teste_mapa_completo(self):
        mapa = cinzas.Mapa("""
.A...A
......
*....A
        """)
        self.assertEquals(mapa.some_primeiro_aeroporto(), 3)
        self.assertEqual(mapa.some_todos_aeroportos(), 7)


unittest.main()