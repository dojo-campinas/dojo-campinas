def campo_minado(mapa):
    resultado = mapa.replace("_","0")

    if "*" in mapa:
        linhas = resultado.split()
        matriz = [list(i) for i in linhas]
        for linha, conteudo in enumerate(matriz):
            for coluna, caracter in enumerate(conteudo):
                if caracter == "*":
                    try:
                        if linha-1 < 0:
                            raise IndexError
                    
                        norte = matriz[linha-1][coluna]
                        if norte != "*":
                            matriz[linha-1][coluna] = str(int(norte) + 1)
                    except IndexError: 
                        pass
                        
                    try:
                        if linha-1 < 0:
                            raise IndexError
                        if coluna-1 < 0:
                            raise IndexError
                    
                        noroeste = matriz[linha-1][coluna-1]
                        if noroeste != "*":
                            matriz[linha-1][coluna-1] = str(int(noroeste) + 1)
                    except IndexError: 
                        pass
                        
                    try:
                        if linha-1 < 0:
                            raise IndexError
                        nordeste = matriz[linha-1][coluna+1]
                        if nordeste != "*":
                            matriz[linha-1][coluna+1] = str(int(nordeste) + 1)
                    except IndexError:
                        pass 
                      
                    try:
                        leste = matriz[linha][coluna+1]
                        if leste != "*":
                            matriz[linha][coluna+1] = str(int(leste) + 1)
                    except IndexError: 
                        pass
                        
                    try:    
                        sul = matriz[linha+1][coluna]
                        if sul != "*":
                            matriz[linha+1][coluna] = str(int(sul) + 1)
                    except IndexError: 
                        pass
                        
                    try:    
                        sudeste = matriz[linha+1][coluna+1]
                        if sudeste != "*":
                            matriz[linha+1][coluna+1] = str(int(sudeste) + 1)
                    except IndexError:
                        pass
                 
                    try:
                        if coluna-1 < 0:
                            raise IndexError
                        oeste = matriz[linha][coluna-1]
                        if oeste != "*":
                            matriz[linha][coluna-1] = str(int(oeste) + 1)
                    except IndexError:
                        pass
                 
                    try:    
                        if coluna-1 < 0:
                            raise IndexError
                        sudoeste = matriz[linha+1][coluna-1]
                        if sudoeste != "*":
                            matriz[linha+1][coluna-1] = str(int(sudoeste) + 1)
                    except IndexError:
                        pass
                       
        return "\n".join(["".join(line) for line in matriz])
    return resultado
