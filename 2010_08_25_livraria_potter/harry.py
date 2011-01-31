CUSTO_UNITARIO = 42
DESCONTO = [ 1, 
             1,
             1-0.05,
             1-0.07,
             1-0.09,
             1-0.11 ]

def livraria(lista_livros):
    livros = [int(i) for i in lista_livros.split() if int(i) != 0]   #listas compreensivas
    
    qtde_minima = min(livros) if livros else 0    
    qtde_titulos = len(livros)
    
    if qtde_titulos > 1:
        # soma o desconto dos grupos
        preco = qtde_minima * CUSTO_UNITARIO * DESCONTO[qtde_titulos] * qtde_titulos
        
        # soma livros restantes(sobras)
        preco += (max(livros) - qtde_minima) * CUSTO_UNITARIO
    else:
        preco = CUSTO_UNITARIO * sum(livros)
    
    return preco
