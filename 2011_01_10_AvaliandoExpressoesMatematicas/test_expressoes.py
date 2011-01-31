#!/usr/bin/env python
# -*- encoding: utf-8 -*- 

import unittest
from expressoes import Expressao

class ExpressoesMatematicasTestCase(unittest.TestCase): 

    def teste_deve_instanciar_uma_expressao(self):
        self.assertTrue(isinstance(Expressao(""), Expressao))

    def teste_deve_possuir_lista_de_tokens(self):
        expr = Expressao("")
        self.assertTrue(hasattr(expr, "tokens"))
        self.assertTrue(isinstance(expr.tokens, list))

    def teste_deve_tokenizar_numeros_de_um_digito(self):
        expr = Expressao("4")
        # primeiro token da lista de tokens tem que ser o numero 4
        self.assertEquals(expr.tokens[0], 4)

    def teste_deve_ler_numero_decimal(self):
        expr = Expressao("1.5")
        # primeiro token da lista de tokens tem que ser o decimal 1.5
        self.assertEquals(expr.tokens[0], 1.5)
       
    def teste_deve_ignorar_espaco(self):
        expr = Expressao(" ")
        self.assertEquals(expr.tokens, [])

    def teste_deve_tokenizar_soma(self):
        expr = Expressao(" 1 + 1 ")
        self.assertEquals(len(expr.tokens), 3)
        self.assertTrue("+" in expr.tokens)

    def teste_deve_tokenizar_subtracao(self):
        expr = Expressao("1-1")
        self.assertEquals(len(expr.tokens), 3)
        self.assertTrue("-" in expr.tokens)

    def teste_deve_tokenizar_operadores_seguidos(self):
        expr = Expressao("1 + (1)")
        self.assertEquals(expr.tokens, [1, "+", "(", 1, ")"])

    def teste_deve_tokenizar_expressao_complexa(self):
        expr = Expressao("2 + 5 *(7 * 10 + 5.7 -10)")
        self.assertEquals(expr.tokens, [2, "+", 5, "*", "(", 7, "*", 10, "+", 5.7, "-", 10,")"])

    def teste_deve_avaliar_uma_soma(self):
        expr = Expressao("1+1")
        self.assertEquals(expr.resolve_expressao(), 2)
        expr = Expressao("20+22")
        self.assertEquals(expr.resolve_expressao(), 42)

    def teste_deve_avaliar_uma_subtracao(self):
        expr = Expressao("3-2")
        self.assertEquals(expr.resolve_expressao(), 1)

    def teste_deve_avaliar_uma_multiplicacao(self):
        expr = Expressao("21*2")
        self.assertEquals(expr.resolve_expressao(), 42)

    def teste_deve_avaliar_uma_divisao(self):
        expr = Expressao("84/2")
        self.assertEquals(expr.resolve_expressao(), 42)

    def teste_deve_separar_operadores_e_operandos(self):
        expr = Expressao("2 + 3")
        self.assertEquals(expr.operadores, ["+"])
        self.assertEquals(expr.operandos, [2,3])

    def teste_deve_somar_varios_operandos(self):
        expr = Expressao("1 + 2 + 3 + 4")
        self.assertEquals(expr.resolve_expressao(), 10)


    def teste_deve_priorizar_operadores(self):
        expr = Expressao("3 * 5 + 9")
        self.assertEquals(expr.resolve_expressao(), 24)    

if __name__ == "__main__":
    unittest.main()

