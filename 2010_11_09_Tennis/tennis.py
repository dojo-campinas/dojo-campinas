GAME_POINT = 40
ADVANTAGE = 'A'
PONTOS = [0, 15, 30, GAME_POINT, ADVANTAGE]
ESTADOS = {
    "EM_ANDAMENTO": "em andamento",
    "VENCEU": "%s venceu",
    "EMPATE": "deuce",
    "VANTAGEM" : "vantagem %s",
}

class Game():
    def __init__(self):
        self._pontos = {}
        self._pontos["jogador1"] = 0
        self._pontos["jogador2"] = 0
        self._estado = ESTADOS["EM_ANDAMENTO"]
    
    def placar(self):
        return (PONTOS[self._pontos["jogador1"]],
                PONTOS[self._pontos["jogador2"]],
                self._estado)
    
    def pontuar(self, jogador):
        if PONTOS[self._pontos[jogador]] == GAME_POINT and self._estado != ESTADOS["EMPATE"]:
            self._estado = ESTADOS["VENCEU"] % jogador
        else:
            self._pontos[jogador] += 1

        if PONTOS[self._pontos['jogador1']] == GAME_POINT \
           and PONTOS[self._pontos['jogador2']] == GAME_POINT:
            self._estado = ESTADOS["EMPATE"]
        elif PONTOS[self._pontos[jogador]] == ADVANTAGE and self._estado == ESTADOS["EMPATE"]:
            self._estado = ESTADOS["VANTAGEM"] % jogador
