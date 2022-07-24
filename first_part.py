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

class RomanNumberError(Exception):
    pass


numero_romano = (
    (1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')
    )

centenas = (
    (100,'C'),(200,'CC'),(300,'CCC'),
    (400,'CD'),(500,'D'),(600,'DC'),
    (700,'DCC'),(800,'DCCC'),(900,'CM')
)

decenas = (
    (10,'X'),(20,'XX'),(30,'XXX'),
    (40,'XL'),(50,'L'),(60,'LX'),
    (70,'LXX'),(80,'LXXX'),(90,'XC')
)

unidades = (
    (1,'I'),(2,'II'),(3,'III'),
    (4,'IV'),(5,'V'),(6,'VI'),
    (7,'VII'),(8,'VIII'),(9,'IX')
)

'''
Segunda solución con funciones
def letras_numeros_romanos(cantidad):
    if cantidad == 'miles':
        return ('M','','')
    elif cantidad == 'centenas':
        return ('C','D','M')
    elif cantidad == 'decenas':
        return ('X','L','C')
    elif cantidad == 'unidades':
        return ('I','V','X')

def digito_decimal_a_digito_romano(numero,cantidad):
    caract_romanos = letras_numeros_romanos(cantidad)
    if numero < 4:
        return caract_romanos[0] * numero
    elif numero == 4:
        return caract_romanos[0] + caract_romanos[1]
    elif numero < 9:
        return caract_romanos[1] + caract_romanos[0] * (numero-5)
    else:
        return caract_romanos[0] + caract_romanos[2]

def entero_a_romano(num):
    numero_romano = ''
    longitud = {4:'miles',3:'centenas',2:'decenas',1:'unidades'}
    num = list(num)
    for pos,i in enumerate(num):
        numero_romano = numero_romano + digito_decimal_a_digito_romano(int(i),longitud[len(num)-pos])
    return numero_romano
'''

def entero_a_romano(numero):

    numero = '{:0>4d}'.format(numero)
    digitos = list(numero)

    longitud = len(digitos)
    for ix in range(longitud):
        longitud -= 1
        digitos[ix] = digitos[ix] + '0' * longitud

    return digitos
 

entero_a_romano(336)

#numero_decimal = input("Elige un número entre 1 y 3999: ")

#print(entero_a_romano(numero_decimal))
