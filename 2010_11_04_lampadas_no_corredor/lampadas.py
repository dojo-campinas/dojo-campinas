# Lampadas no corredor

def inverte_interruptor(valor):
	if valor == 'off':
		valor = 'on'
	else:
		valor = 'off'
	return valor

def lampada(n):
	lista = n * ['off']

	for ida in range(1, n + 1):
		for lampada_corrente in range(1, n + 1):
			if lampada_corrente % ida == 0:
				lista[lampada_corrente - 1] = inverte_interruptor(lista[lampada_corrente - 1])

	return lista	
