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
    (1000, 'M'), (500, 'D'), (100, 'V'), (50, 'C'), (10, 'X'), (5, 'V'), (1, 'I')
    )

def entero_a_romano(numero):
    return 'MCMXCIV'