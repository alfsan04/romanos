def letras_numeros_romanos(pos):
    '''pos-> 0 es miles, 1 es centenas, 2 es decenas, 3 es unidades.
    Devuelvo tupla con uno, cinco y diez en romano
    posiciones de valores_romanos que necesito en funcion de pos y tuplas que devuelve
    pos 0 -> 2, 1, 0 -> ('M','','')
    pos 1 -> 4, 3, 2 -> ('C','D','M')
    pos 2 -> 6, 5, 4 -> ('X','L','C')
    pos 3 -> 8, 7, 6 -> ('I','V','X')
    '''
    valores_romanos = ('', '', 'M', 'D', 'C', 'L', 'X', 'V', 'I')
    return('', valores_romanos[pos*2+2], valores_romanos[pos*2+1], valores_romanos[pos*2])

def digito_decimal_a_digito_romano(numero,pos):
    caract_romanos = letras_numeros_romanos(pos) #tupla recibida: (cero,uno,cinco,diez) en romanos
    if numero%5 == 4:
        return caract_romanos[1] + caract_romanos[2+(numero//5)]
    else:
        return caract_romanos[(numero//5)*2] + caract_romanos[1] * (numero%5)

def entero_a_romano(numero_decimal):
    numero_romano = ''
    for pos,valor in enumerate(list(str(numero_decimal))):
        numero_romano += digito_decimal_a_digito_romano(int(valor),pos+(4-len(str(numero_decimal))))
    return numero_romano

print(entero_a_romano(1336))