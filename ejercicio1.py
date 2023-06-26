empleados = open('ejercicio1.txt','w')
nombre = ('')
apellido = ('')
email = ('')
opc = 1

while opc != 3:
    print('\n1: Ingresar nombre, apellido y mail del empleado')
    print('2: Mostrar los empleados ingresados hasta el momento')
    print('3: Salir y mostrar todos los empleados\n')
    opc = int(input('Ingrese una nueva opción: '))
    
    if opc == 1:
        empleados = open('ejercicio1.txt','a')
        print('Ingrese los datos de un empelado debajo:')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        email = input('Email: ')
        
        empleados.write(f'\nEl empleado {nombre}, de apellido: {apellido} con su email:{email}')
        empleados.close()
    elif opc == 2:
        empleados = open('ejercicio1.txt','r')
        texto = empleados.read()
        print(texto)
        empleados.close()
    elif opc == 3:
        break
    else:
        print('Opción no valida, ingrese una opción valida')
        print('Ingrese la opción que usted desee: ')

empleados = open('ejercicio1.txt','r')
texto = empleados.read()
print(f'Los contactos en la lista son: {texto}')
empleados.close()

empleados.close()