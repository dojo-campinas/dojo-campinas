import unittest

from lampadas import lampada
from lampadas import inverte_interruptor

class LampadasTest(unittest.TestCase):

    def test_corredor_com_1_interruptor(self):
        self.assertEquals(lampada(1), ['on'])

    def test_corredor_com_2_interruptores(self):
        self.assertEquals(lampada(2), ['on', 'off'])

    def test_corredor_com_3_interruptores(self):
        self.assertEquals(lampada(3), ['on', 'off', 'off'])

    def test_corredor_com_4_interruptores(self):
        self.assertEquals(lampada(4), ['on', 'off', 'off', 'on'])
    
    def test_corredor_com_5_interruptores(self):
        self.assertEquals(lampada(5), ['on', 'off', 'off', 'on', 'off'])

    def test_inversor(self):
        self.assertEquals(inverte_interruptor('on'), 'off')
        self.assertEquals(inverte_interruptor('off'), 'on')

if __name__ == '__main__':
    unittest.main()

