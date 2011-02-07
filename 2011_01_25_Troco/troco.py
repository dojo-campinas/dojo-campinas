


def devolve_troco(valor_pago, valor_total):
    moedas_disponiveis = ['100.00', '50.00', '10.00', '5.00', '1.00', '0.50', '0.10', '0.05', '0.01']
    troco = round (valor_pago - valor_total, 2)

    moedas = {}
    for moeda in moedas_disponiveis:
       conta_moedas = 0
       while round(troco, 2) >= round(float(moeda), 2):
           troco -= float(moeda)
           conta_moedas += 1
       if conta_moedas > 0:
           moedas[moeda] = conta_moedas
    #print moedas
    return moedas
        
