# UPE - Programacion en tiempo real 2021
# Diagnostico inicial
# Ejercicio 4
"""
Desarrollar el código Python que solicite al usuario un número X de entre 1 y 100,
que cree un vector de X posiciones y solicite al usuario ingresar los X valores que se
deberán incluir en el vector.. Se deberá validar que X este entre 1 y 100. Caso
contrario, informar al usuario y volver a pedir que ingrese X.

"""

def main():
    num = int(input('Ingrese tamaño del vector - numero entre 1 y 100: '))
    while num < 1 or num > 100:
        num = int(input('El numero no esta entre 1 y 100, ingrese nuevamente: '))
    
    # Lleno la lista
    lista = []
    for n in range(1, num+1):
        lista.append(int(input(f'Ingrese valor posicion {n} :')))
    
    # Muestro la lista
    print(f'Se genero la lista con {num} posiciones: {lista}')


if __name__ == '__main__':
    main()
    
    