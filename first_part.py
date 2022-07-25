'''
1. Crear una función que pase de entero > 0 y < 4000 a romano
2. Cualquier otra entrada debe dar error

Casos de prueba
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor es mayor de 3999")
c) "unacadena" -> RomanNumberError("Debe ser un entero")
d) 0 -> RomanNumberError("El valor debe ser mayor de cero")
e) -3 -> RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")

'''

'''
Segunda solución con funciones
def letras_numeros_romanos(pos):
    #pos -> 0: miles, 1: centenas, 2: decenas, 3: unidades
    if pos == 0:
        return ('M','','')
    elif pos == 1:
        return ('C','D','M')
    elif pos == 2:
        return ('X','L','C')
    elif pos == 3:
        return ('I','V','X')

def digito_decimal_a_digito_romano(numero,pos):
    caract_romanos = letras_numeros_romanos(pos)
    if numero < 4:
        return caract_romanos[0] * numero
    elif numero == 4:
        return caract_romanos[0] + caract_romanos[1]
    elif numero < 9:
        return caract_romanos[1] + caract_romanos[0] * (numero-5)
    else:
        return caract_romanos[0] + caract_romanos[2]

def entero_a_romano(numero_decimal):
    numero_romano = ''
    for pos,valor in enumerate(list(str(numero_decimal))):
        numero_romano += digito_decimal_a_digito_romano(int(valor),pos+(4-len(str(numero_decimal))))
    return numero_romano
'''

class RomanNumberError(Exception):
    pass


numero_romano = (
    (1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')
    )

componentes = {
        1000: 'M', 2000: 'MM', 3000: 'MMM',
        100:'C',200:'CC',300:'CCC',
        400:'CD',500:'D',600:'DC',
        700:'DCC',800:'DCCC',900:'CM',
        10:'X',20:'XX',30:'XXX',
        40:'XL',50:'L',60:'LX',
        70:'LXX',80:'LXXX',90:'XC',
        1:'I',2:'II',3:'III',
        4:'IV',5:'V',6:'VI',
        7:'VII',8:'VIII',9:'IX'
}

def entero_a_romano(numero):

    numero = '{:0>4d}'.format(numero)
    digitos = list(numero)

    longitud = len(digitos)
    romano = '' 
    for ix in range(len(numero)):
        longitud -= 1
        digitos[ix] = digitos[ix] + '0' * longitud
        romano += componentes.get(int(digitos[ix]), '')

    return romano

print(entero_a_romano(1336))
