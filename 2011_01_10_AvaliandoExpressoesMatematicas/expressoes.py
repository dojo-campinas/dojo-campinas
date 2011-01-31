#!/usr/bin/env python
#-*- encoding: utf-8 -*-

class Expressao():
    def __init__(self, cadeia):
        self.tokens = []
        self.cadeia = cadeia.replace(" ", "")
        self.tokenizador()
        self.define_pilhas()

    def tokenizador(self):
        if self.cadeia:
            buffer_numero = ""
            for caractere in self.cadeia:
                if caractere.isdigit():
                    buffer_numero += caractere
                elif caractere == '.':
                    buffer_numero += caractere
                elif buffer_numero:
                    self.tokens.append(float(buffer_numero))
                    buffer_numero = ""
                    #Se não for ponto ou digito, é um operador
                    self.tokens.append(caractere)   
                else:
                    self.tokens.append(caractere)

            if buffer_numero:
                self.tokens.append(float(buffer_numero))

    def define_pilhas(self):
        self.operadores = []
        self.operandos = []
        for tok in self.tokens:
            if isinstance(tok, float):
                self.operandos.append(tok)
            else:
                self.operadores.append(tok)
        

    def resolve_expressao(self):
        operadores_aux = []
        for i, operador in enumerate(reversed(self.operadores)):
                 
            if operador == "*":
                op1 = self.operandos.pop(i-1)
                op2 = self.operandos.pop(i-1)
                result = op2 * op1
                self.operandos.insert(i-1, result)
            elif operador == "/":
                op1 = self.operandos.pop(i-1)
                op2 = self.operandos.pop(i-1)
                result = op2 / op1
                self.operandos.insert(i-1, result)
            else:
                operadores_aux.append(operador)

        for i, operador in enumerate(operadores_aux):
            if operador == "+":
                op1 = self.operandos.pop()
                op2 = self.operandos.pop()
                result = op2 + op1
                self.operandos.append(result)
            elif operador == "-":
                op1 = self.operandos.pop()
                op2 = self.operandos.pop()
                result = op2 - op1
                self.operandos.append(result)

        return self.operandos.pop()

