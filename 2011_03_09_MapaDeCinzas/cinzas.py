# -*- coding: utf-8 -*-

class Mapa(object):
    def __init__(self, mapa):
        mapa = mapa.strip()
        linhas = mapa.split("\n")
        self.linhas = []
        for linha in linhas:
            self.linhas.append(bytearray(linha))
        
        self.altura = len(self.linhas)
        self.largura = len(self.linhas[0])

    def conta_aeroportos(self):
        num_aeroportos = 0

        for linha in self.linhas:
            num_aeroportos += linha.count("A")

        return num_aeroportos

    def __getitem__(self, indice):
        coluna = indice[0]
        linha = indice[1]
        try:
            return chr(self.linhas[linha][coluna])
        except IndexError: 
            return None

    def __setitem__(self, indice, valor):
        coluna = indice[0]
        linha = indice[1]
        if linha < 0 or coluna < 0:
            return 
        try:
            self.linhas[linha][coluna] = valor
        except IndexError: pass

    def passa_dia(self):
        for y, linha in enumerate(self.linhas):
            for x, elemento in enumerate(linha):
                if chr(elemento) == '*':
                    if self[x-1, y] != '*':
                        self[x-1, y] = 'x'
                    if self[x+1, y] != '*':
                        self[x+1, y] = 'x'
                    if self[x, y-1] != '*':
                        self[x, y-1] = 'x'
                    if self[x, y+1] != '*':
                        self[x, y+1] = 'x'
                        
        for y, linha in enumerate(self.linhas):
            for x, elemento in enumerate(linha):
                if chr(elemento) == "x":
                    self[x, y] = "*"

    def some_primeiro_aeroporto(self):
        total = self.conta_aeroportos()

        if total == 0:
            return None

        mapa = self.copy()

        i = 0
        while mapa.conta_aeroportos() == total:
            mapa.passa_dia()
            i += 1

        return i

    def some_todos_aeroportos(self):
        total = self.conta_aeroportos()
        if total == 0:
            return None
        mapa = self.copy()
        i = 0
        while mapa.conta_aeroportos() > 0:
            mapa.passa_dia()
            print mapa
            print
            i += 1

        return i

    def copy(self):
        return Mapa(str(self))

    def __repr__(self):
        return "\n".join(str(linha) for linha in self.linhas)
