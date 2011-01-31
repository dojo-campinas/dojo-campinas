import unittest

def Jokenpo(item1, item2):
    if item1 == item2: return 'empate'
    
    if 'tesoura' in (item1, item2):
        if 'pedra' in (item1, item2):
            return 'pedra'
        else: 
            return 'tesoura' 
        
    if 'papel' in (item1, item2):
        if 'pedra' in (item1, item2):
            return 'papel'
        else:
            return 'tesoura'      

class JoKenPoTest(unittest.TestCase):
    def testeSeEmpate(self):
        self.assertEquals(Jokenpo('tesoura','tesoura'),'empate')
        
    def testeSeTesouraVencePapel(self):
        self.assertEquals(Jokenpo('tesoura','papel'),'tesoura')
        
    def testeSePapelVencePedra(self):
        self.assertEquals(Jokenpo('pedra','papel'),'papel')
        
    def testeSePedraVenceTesoura(self):
        self.assertEquals(Jokenpo('pedra', 'tesoura'), 'pedra')
        
    
if __name__ == "__main__":
    unittest.main()
