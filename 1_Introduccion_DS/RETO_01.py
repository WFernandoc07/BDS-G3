"""
CREAR UN PROGRAMA QUE PUEDA CONVERTIR MONEDAS DE SOLES A DOLARES O DE DOLARES A SOLES ,
USE CONDICIONLAES Y BUCLES Y AL FINAL EL PROGAMA DEBE PREGUNTAR SI DFESEA CONTINUAR, SI NO , 
SALE RECIEN DEL PROGRAMA
"""
monto = input('Ingrese el monto a convertir: ')

opcion = input('Elija una Opción:'
                  '\n\tOPCIÓN 1: Convertir Soles a Dólares'
                  '\n\tOPCIÓN 2: Convertir de Dólares a Soles\nOPCION = ')

while opcion != '1' or opcion != '2':
    if opcion == '1':
        print(f'El Monto $ {float(monto)} al convertir de Soles a Dólares es: {float(monto) / 3.75}\n')
    elif opcion == '2':
        print(f'El S/. {float(monto)} al convertir de Dólares a Soles es: {float(monto) * 3.74}\n')
    else:
        print('Opción no válida, intente de nuevo')
    continuar = input('¿Desea Continuar? S/N: ')
    if continuar.upper() == 'S':
        monto = input('Ingrese el monto a convertir: ')
        opcion = input('Elija una Opción:'
                      '\n\tOPCIÓN 1: Convertir Soles a Dólares'
                      '\n\tOPCIÓN 2: Convertir de Dólares a Soles\nOPCION = ')
    else:
        break

