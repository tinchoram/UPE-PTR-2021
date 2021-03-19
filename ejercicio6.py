# UPE - Programacion en tiempo real 2021
# Diagnostico inicial
# Ejercicio 6
"""
Desarrollar el código de un programa Python para calcular el factorial de un número
(que deberá solicitar al usuario) utilizando recursividad.

"""

def factorial(num):
    """
    Calcula factorial de param:num
    """
    if num == 1:
        return 1
    
    return num * factorial(num-1)


if __name__ == '__main__':
    num = int(input('Ingrese un numero: '))
    num_factorial = factorial(num)
    print(f'El factorial de {num} es: {num_factorial}')
    