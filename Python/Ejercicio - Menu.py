from math import*

inicio=True
while inicio:
   print('\nMenu:')
   print('a)Calcular diàmetro')
   print('b)Calcular perìmetro')
   print('c)Calcular àrea')
   print('d)Salir\n')
   print('Seleccione la opciòn deseada: ')
   orden=input()

   if orden=='d':
      inicio=False
   else:
      print('Introduzca el valor del radio:')
      r=float(input())
      if orden=='a':
         print('El diàmetro es: ', r*2)
      elif orden=='b':
         print('El perìmetro es: ', r*2*pi)
      elif orden=='c':
         print('El àrea es: ', r*r*pi)
      else:
         print('<Error> Seleccione una opciòn vàlida')
print('Gracias por utilizar el programa :)')
