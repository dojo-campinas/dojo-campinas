#-*- coding: utf-8 -*-

def retorna_mapa(mapa):
    for linha in enumerate(mapa):
        for coluna in enumerate(linha):
            if mapa[linha[0]][coluna[0]] == '.':
                mapa[linha[0]][coluna[0]] = '0'
            elif mapa[linha[0]][coluna[0]] == '*':
                mapa[linha[0]][coluna[0]] = '0'
                mapa[linha[0]][coluna[0]] = '0'
                mapa[linha[0]][coluna[0]] = '0'
                mapa[linha[0]][coluna[0]] = '0'
                
    return mapa
    
    
#    if mapa[0][0] == '*':
#        if mapa[1][1] == '*':
#            return [['*','2'],['2','*'],]
#        else:
#            return [['*','1'],['1','1'],]
#    else:
#        return [['0','0'],['0','0'],]
