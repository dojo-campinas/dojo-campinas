# coding: utf-8
class Relogio(object):

    def __init__(self, horario=None):
        self.data = self._blank()
        if horario is not None:
            self.hora = int(horario.split(":")[0])
            self.add_hora()
            self.add_minuto(horario)

    def add_hora(self):
        self.data[self.hora] = "h"
        
    def add_minuto(self, minuto):
        self.data[3] = "m"
        
    def _blank(self):
        return bytearray('oooooooooooo')
