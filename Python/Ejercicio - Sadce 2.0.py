def innum ():
   while True:
      try:
         x=int(input('> '))
         break
      except ValueError:
         print('<ERROR: VALOR NO VÁLIDO>')
   return (x)

def registro():
    print('Registro de alumnos')
    n1=input('NOMBRE:           ')
    n2=input('APELLIDO PATERNO: ')
    n3=input('APELLIDO MATERNO: ')
    n1=n1.replace(' ','')
    n2=n2.replace(' ','')
    n3=n3.replace(' ','')
    apellido.append(n2.title())
    nombre.append(n1+' '+n2+' '+n3)
    matricula.append(len(matricula)+200118000)
    print('\nSu matrícula es: ',len(matricula)+200117999)
    print('\nREGISTRO COMPLETADO')
    return()

def edicion(pos):
    ant_nombre=nombre[pos]
    nombre.pop(pos)
    apellido.pop(pos)
    
    print('\nIngrese los nuevos datos')
    n1=input('NOMBRE:           ')
    n2=input('APELLIDO PATERNO: ')
    n3=input('APELLIDO MATERNO: ')
    n1=n1.replace(' ','')
    n2=n2.replace(' ','')
    n3=n3.replace(' ','')
    apellido.append(n2)
    nombre.append(n1+' '+n2+' '+n3)
    print('\nSE HAN GUARDADO LOS CAMBIOS')
    print(ant_nombre,' => ',' ',nombre[pos],' ',matricula[pos])
    
    return()

def buscar(x,lista):
    res=' no fue encontrad'
    for i in range (len(lista)):
        if x==lista[i]:
            res=i
            res=str(res)
            break
    return (res)

nombre=[]
apellido=[]
matricula=[]
calificaciones=[]

contraseña='uwu'

op=0
#menu de inicio
while op != 7:
    print('\nSelecione una opción')
    print('1) Registrar alumno')
    print('2) Consultar alumno')
    print('3) Editar alumnos')
    print('4) Eliminar alumnos')
    print('5) Calificaciones')
    print('6) Cambiar contraseña')
    print('7) Salir')
    
    op=innum()
    print('')

#registro de alumnos
    if op==1:
        registro()

#consulta de alumnos
    elif op==2:
        opc=0
        if len(matricula)==0:
            print('<No hay alumnos registrados>')
            opc=4

        while opc!=4:
            print('Selecione una opción de consulta')
            print('1) Consultar por matrícula')
            print('2) Consultar por apellido')
            print('3) Consultar todos')
            print('4) Regresar')
        
            opc=innum()

        #consulta por matricula
            if opc==1:
                print('\nIntroduzca la matrícula del alumno:')
                matricula_bus=innum()
                pos=buscar(matricula_bus, matricula)

                if pos.isnumeric():
                    pos=int(pos)
                    print('\nNombre:    ', nombre[pos])
                    print('Matrícula: ', matricula[pos],'')
                    opc=4
                else:
                    print('\nLa matrícula: ',matricula_bus, pos+'a\n')
                    opc=1
        
        #consulta por apellido
            elif opc==2:
                print('\nIntroduzca el apellido del alumno:')
                apellido_bus=input('> ')
                print('')
                apellido_bus.title()

                cont=0
                for i in range (len(apellido)):
                    if apellido_bus==apellido[i]:
                        print(matricula[i],' ',nombre[i])
                        cont+=1
                        opc=4
                if cont==0:
                    print('\nEl apellido: ',apellido_bus,' no fue encontrado')
                    print('Asegurese de que el apellido este correcto\n')
                    opc=2
        
        #imprime todos los alumnos
            elif opc==3:
                print('')
                for i in range(len(matricula)):
                    print(matricula[i],' ',nombre[i])
                opc=4

        #opcion de omisión     
            elif (opc!=1)&(opc!=2)&(opc!=3)&(opc!=4):
                print('\n<Opción no valida>\n')

#Editar alumnos
    elif op==3:
        if len(matricula)==0:
            print('<No hay alumnos registrados>')
        else:
           while True:
                print('Introduzca la matrícula del alumno:')
                matricula_bus=innum()
                pos=buscar(matricula_bus, matricula)

                if pos.isnumeric():
                    pos=int(pos)
                    print('\nDesea editar el registro: ',matricula[pos],' ',nombre[pos])
                    decision=input('S/N >>> ')
                    decision=decision.upper()
                    print('')

                    while not((decision=='S')or(decision=='N')):
                        print('<Opción no valida>')
                        decision=input('S/N >>> ')
                        decision=decision.upper()
            
                    if (decision=='S'):
                        edicion(pos)
                    break
                else:
                    print('\nLa matrícula: ',matricula_bus, pos+'a\n')
                
#Eliminar alumnos
    elif op==4:
        if len(matricula)==0:
            print('<No hay alumnos registrados>')
        else:
            while True:
                print('Introduzca la matrícula del alumno:')
                matricula_bus=innum()
                pos=buscar(matricula_bus, matricula)

                if pos.isnumeric():
                    pos=int(pos)
                    print('\nEsta seguro que desea eliminar al alumno: ',matricula[pos],' ',nombre[pos])
                    decision=input('S/N >>> ')
                    decision=decision.upper()

                    while not((decision=='S')or(decision=='N')):
                        print('<Opción no valida>')
                        decision=input('S/N >>> ')
                        decision=decision.upper()
            
                    if (decision=='S'):
                        print('\nEl alumno: ',matricula[pos],' ',nombre[pos],' ha sido eliminado de la base de datos')
                        matricula.pop(pos)
                        nombre.pop(pos)
                        apellido.pop(pos)
                    break
                else:
                    print('\nLa matrícula: ',matricula_bus, pos+'a\n')
                     
#Calificaciones
    elif op==5:
        while True:
            print('\nSelecione una opción')
            print('1) Registrar calificaciones')
            print('2) Consultar calificaciones')
            print('3) Editar calificacinoes')
            print('4) Regresar')
            opcal=innum()
            print('')
            
            if opcal==1:
                
            elif opcal==2:

            elif opcal==3:
                
            elif opcal==4:
                break
            else:
                print('<Opción no cálida>')

#Cambiar ccontraseña
    elif op==6:
        while True:
            print('Ingrese la contraseña')
            contraseña_antigua=input('> ')
            if contraseña_antigua==contraseña:
                print('\nIngrese la nueva contraseña')
                contraseña=input('> ')
                print('\nLos cambios se han guardado')
                break
            else:
                print('\n<La contraseña es incorrecta>')

#Salir    
    elif op==7:
        print('Hasta luego :D')

#Opcion de omisión
    else:
        print('<Opción no valida>')