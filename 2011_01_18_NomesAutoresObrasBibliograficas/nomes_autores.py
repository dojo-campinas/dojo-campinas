

def converte (nome):
    aux_nome = nome.split(" ")
    if len(aux_nome) == 1:
        return nome.upper()
    if len(aux_nome) == 2:
        aux_nome = aux_nome[-1].upper() + ", " + aux_nome[0]
    else:
        parentesco = ['FILHO', 'JUNIOR', 'SOBRINHO', 'NETO', 'FILHA', 'NETA', 'SOBRINHA']
        if aux_nome[-1].upper() in parentesco:
            aux_nome = "{0} {1}, {2}".format(aux_nome[-2].upper(),  aux_nome[-1].upper(), aux_nome[-3])
        else:
            aux_nome = "{0}, {1} {2}".format(aux_nome[-1].upper(), aux_nome[-3], aux_nome[-2])
    return aux_nome  
