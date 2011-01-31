_IS_NOT_PRIME = 'It is not a prime word.'
_IS_PRIME = 'It is a prime word.'

from string import ascii_letters

def funcao_palavra_prima(palavra):
    valor = 0
    for letra_da_palavra in palavra:
        valor += ascii_letters.index(letra_da_palavra) + 1
    
    if numero_eh_primo(valor):
        return _IS_PRIME
    else:
        return _IS_NOT_PRIME      
        
def numero_eh_primo(numero):
    if numero <= 2:
        return True
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
    

