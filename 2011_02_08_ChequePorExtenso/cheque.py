# coding: utf-8

def extenso(numero):
    if numero <= 0.00:
        raise ValueError
    reais = int(numero)
    centavos =100* round(numero - reais, 2)
    
    valor_reais= valor_por_extenso(reais)

    if reais >= 1:
        if reais == 1:
            valor_reais = valor_reais + " real"
        else:
            valor_reais = valor_reais + " reais"

    valor_centavos = valor_por_extenso(centavos)
    
    if centavos == 1:
        valor_centavos = valor_centavos + " centavo"
    elif centavos > 1:
        valor_centavos = valor_centavos + " centavos"

    if centavos == 0:
        return valor_reais
    elif reais == 0:
        return valor_centavos

    return valor_reais + " e " + valor_centavos

def valor_por_extenso(numero):
    valores_unidade = {
        0: "",
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        }
    valores_teens = {
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove",
    }

    valores_dezenas = {
        10: "dez",
        20: "vinte",
        30: "trinta",
        40: "quarenta",
        50: "cinquenta",
        60: "sessenta",
        70: "setenta",
        80: "oitenta",
        90: "noventa",
    }

    valores_centenas = {
        100: "cento",
        200: "duzentos",
        300: "trezentos",
        400: "quatrocentos",
        500: "quinhentos",
        600: "seiscentos",
        700: "setecentos",
        800: "oitocentos",
        900: "novecentos",
    }

    
    resultado = ""
    
    if numero == 100:
        resultado = "cem"
        numero = 0
    elif numero > 100:
        resultado = valores_centenas[numero - numero % 100]
        numero -= round(numero // 100) * 100
        if numero:
            if resultado:
                resultado += " e "
    if 20 <= numero < 100:
        resultado += valores_dezenas[numero - numero % 10]
        numero -= round(numero // 10)  * 10
    elif 10 <= numero < 20:
        resultado += valores_teens[numero]
        numero -= numero

    if numero:
        if resultado and resultado.strip()[-2:] != ' e':
            resultado += " e "
        resultado += valores_unidade[numero]
    return resultado

