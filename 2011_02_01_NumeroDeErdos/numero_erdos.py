#!/usr/bin/env python
# coding: utf-8

# entrada: linhas de publicações
# primeira coluna é o título entre aspas e as demais colunas
#  separadas por vírgula (nomes de autor)
# O autor Erdos tem número de Erdos

import sys

def retorna_erdos(entrada):
    saida = {}
    autores_relacionados = {}  # dicionario de autores pra cada autor
    for publicacao in entrada:
        for autor in publicacao[1:]:
            conj = set(publicacao[1:])  # todos os autores
            conj.remove(autor)
            if autor in autores_relacionados:
                autores_relacionados[autor].update(conj)
            else:
                autores_relacionados[autor] = conj

            saida[autor] = None
            if autor == "Erdos":
                saida[autor] = 0
            else:
                saida[autor] = None
    acabou = False
    contador = 0
    while not acabou and contador < len(entrada):
        acabou=True
        for autor in saida:
            if saida[autor] == None:
                erdos = sys.maxint
                for autor_relacionado in autores_relacionados[autor]:
                    if saida[autor_relacionado] is not None and saida[autor_relacionado] + 1 < erdos:
                        erdos = saida[autor_relacionado] + 1
                if erdos < sys.maxint:
                    saida[autor] = erdos
                else:
                    acabou= False
        contador += 1

    return saida

def parse_line(line):
    pass
