import unittest

from tennis import Game

class TennisTestCase(unittest.TestCase):
    def pontuar_jogador(self, jogador, n):
        for i in xrange(n):
            self.game.pontuar(jogador)    

    def setUp(self):
        self.game = Game()

    def test_se_placar_inicial_eh_zero(self):
        self.assertEquals(self.game.placar(), (0, 0, "em andamento"))
            
    def test_jogador1_pontuando(self):
        self.game.pontuar('jogador1')
        self.assertEquals(self.game.placar(), (15, 0, "em andamento"))

        self.game.pontuar('jogador1')
        self.assertEquals(self.game.placar(), (30, 0, "em andamento"))

        self.game.pontuar('jogador1')
        self.assertEquals(self.game.placar(), (40, 0, "em andamento"))

    def test_jogador2_pontuando(self):
        self.game.pontuar('jogador2')
        self.assertEquals(self.game.placar(), (0, 15, "em andamento"))

    def test_jogador1_pontua_e_depois_jogador2_pontua(self):
        self.game.pontuar('jogador1')
        self.game.pontuar('jogador2')
        self.assertEquals(self.game.placar(), (15, 15, "em andamento"))

    def test_jogador1_vencedor(self):
        self.pontuar_jogador('jogador1', 4)
        self.assertEquals(self.game.placar()[2], "jogador1 venceu")

    def test_jogador2_vencedor(self):
        self.pontuar_jogador('jogador2', 4)
        self.assertEquals(self.game.placar()[2], "jogador2 venceu")

    def test_empate(self):
        self.pontuar_jogador('jogador1', 3)
        self.pontuar_jogador('jogador2', 3)
        self.assertEquals(self.game.placar(), (40, 40, "deuce"))

    def test_jogador1_pontua_no_empate(self):
        self.pontuar_jogador('jogador1', 3)
        self.pontuar_jogador('jogador2', 3)
        self.pontuar_jogador('jogador1', 1)
        self.assertEquals(self.game.placar(), ('A', 40, "vantagem jogador1"))

if __name__ == '__main__':
    unittest.main()

