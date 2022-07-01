print('¿Cuántos alumnos hay en el grupo?')
N=int(input())
suma=0
if (N==0):
    print('El promedio de edad de un grupo sin estudiantes es 0')
else:
    print('Introduzca las endades de los alumnos:')
    for x in range(0,N):
        edad=int(input())
        suma += edad
    print('El promedio de edad del grupo es: ',suma/N)
