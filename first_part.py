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
Mi solución
def entero_a_romano(numero):
    descomposicion = []
    for pos, car in enumerate(str(numero)):
        if len(str(numero))-pos == 4:
            multipl = 1000
        elif len(str(numero))-pos == 3:
            multipl = 100
        elif len(str(numero))-pos == 2:
            multipl = 10
        else:
            multipl = 1
        descomposicion.append(int(car)*multipl)
    numero_romano = ''
    for i in descomposicion:
        if len(str(i)) == 4:
            numero_romano += 'M'*(int(i/1000))
        elif len(str(i)) == 3:
            if i < 400:
                numero_romano += 'C'*(int(i/100))
            elif i == 400:
                numero_romano += 'DC'
            elif i == 500:
                numero_romano += 'D'
            elif i < 900:
                numero_romano += ('D'+('C'*int((i/100)-500)))
            else:
                numero_romano += 'CM'
        elif len(str(i)) == 2:
            if i < 40:
                numero_romano += 'X'*(int(i/10))
            elif i == 40:
                numero_romano += 'XL'
            elif i == 50:
                numero_romano += 'L'
            elif i < 90:
                numero_romano += ('L'+('X'*(int(i/10)-50)))
            else:
                numero_romano += 'XC'
        elif len(str(i)) == 1:
            if i < 4:
                numero_romano += 'I'*i
            elif i == 4:
                numero_romano += 'IV'
            elif i == 5:
                numero_romano += 'V'
            elif i < 9:
                numero_romano += ('V'+('I'*(i-5)))
            else:
                numero_romano += 'IX'
    return descomposicion, numero_romano
'''

'''
Segunda solución con funciones
def dentro_del_numero(posicion):
    if posicion == 'miles':
        return ('M','','')
    elif posicion == 'centenas':
        return ('C','D','M')
    elif posicion == 'decenas':
        return ('X','L','C')
    elif posicion == 'unidades':
        return ('I','V','X')

def numero_a_romano(numero,ubicacion):
    caract_romanos = dentro_del_numero(ubicacion)
    if numero < 4:
        return caract_romanos[0] * numero
    elif numero == 4:
        return caract_romanos[0] + caract_romanos[1]
    elif numero == 5:
        return caract_romanos[1]
    elif numero < 9:
        return caract_romanos[1] + caract_romanos[0] * (numero-5)
    else:
        return caract_romanos[0] + caract_romanos[2]

def entero_a_romano(num):
    numero_romano = ''
    longitud = {4:'miles',3:'centenas',2:'decenas',1:'unidades'}
    num = list(num)
    for pos,i in enumerate(num):
        numero_romano = numero_romano + numero_a_romano(int(i),longitud[len(num)-pos])
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
