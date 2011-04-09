# -*- coding: utf-8 -*-

def proximo_item(n):
    termo = str(n)
    
    if len(termo) > 1:
        cnt = 1
        atual = str(n)[0]
        retorno = ''
        for i in str(n)[1:]:
            if i == atual:
                cnt += 1
            else:
                retorno += str(cnt) + atual
                atual = i
                cnt = 1
        return int(retorno)
    #if len(termo) > 2:
    #    return 31
    #if len(termo) > 1:
    #    if termo[-1] == '1':
    #        return 21
    #    else:
    #        return int("111" + termo[-1])
    else:
       return int("1" + termo)
