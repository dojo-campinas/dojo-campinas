# -*- coding: utf-8 -*-
import re

def leia_cheque(valor):
    if not valor: return ''
    
    if not 'real' in valor and not 'reais' in valor:
        valor = 'zero real ' + valor
        
    r = re.compile(r'(real|reais)', re.I)
    valores = re.split(r, valor)
    
    

    centavos = 0
    if 'centavo' in valores[1]:
        centavos = float(leia_valor(valores[1].strip()))/100
        
    return float(leia_valor(valores[0].strip())) + centavos
    
def leia_valor(valor):
    numeros = {'zero':0, 'um':1, 
    'dois':2, 'tres':3, 
    'quatro':4, 'cinco':5,
    'seis':6,'sete':7,
    'oito':8, 'nove':9,
    'dez': 10, 'onze': 11,
    'doze': 12, 'treze':13,
    'quatorze':14, 'quinze':15,
    'vinte': 20, 'trinta': 30,
    'quarenta': 40, 'cinquenta':50,
    'sessenta':60, 'setenta': 70,
    'oitenta': 80, 'noventa': 90}
    
    l = valor.split() # l = ['vinte', 'e', 'um']
    v = 0

    while 'e' in l: l.remove('e')
    for i in l:
        if i in numeros:
            v += numeros[i]
    
    return v
    
