def innum ():
   while True:
      try:
         x=int(input('> '))
         print('')
         break
      except ValueError:
         print('<ERROR: Valor no válido>\n')
   return (x)

def registro(n):
    while True:
        print('Ingresar el nombre del ciclista con apellido:')
        nom=str(input('> '))
        if nom.isalpha():
            print('\nLa información no esta completa o es incorrecta\n')
        else:
            if ' 'in nom:
                p=nom.replace(' ','')
                if p.isalpha():
                    nombres.append(nom.title())
                    break
                else:
                    print('\nLa información no esta completa o es incorrecta\n')
            else:
                print('\nLa información no esta completa o es incorrecta\n')
    
    while True:
        for i in range (n):
            while True:
                try:
                    a=('Ingrese el tiempo en la etapa '+str(i+1)+': ')
                    x=float(input(a))
                    break
                except ValueError:
                    print('<ERROR: Valor no válido>\n')
            tiempos[i].append(x)
        break
    return()

def mejor(etapa,n):
    t=tiempos[etapa].copy()
    mej=t[n]
    indice=n
    for i in range(n+1,len(t)):
        if mej<t[i]:
            mej=t[i]
            indice=i
    return(indice)

def peor(etapa,n):
    t=tiempos[etapa].copy()
    peor=t[n]
    indice=n
    for i in range(n+1,len(t)):
        if peor>t[i]:
            peor=t[i]
            indice=i
    return(indice)


nombres=[]
tiempos=[[]]

while True:
    print('  Menu Principal')
    print('==================')
    print('1) Registrar')
    print('2) Consultar')
    print('3) Eliminar')
    print('4) Modificar')
    print('5) Salir\n')
    print('Escoja una opción')
    op=innum()

#Registro    
    if op==1:
        if len(nombres)==0:
            registro(1)
        else:
            registro(len(tiempos))

#Consulta            
    elif op==2:
        while True:
            print(' Menu de consulta')
            print('==================')
            print('1) Consultar todo')
            print('2) Consultar tiempos por ciclista')
            print('3) Ganador por etapa')
            print('4) Ganador de la vuelta')
            print('5) Regresar a menu principal\n')
            print('Escoja una opción')
            opc=innum()
            
            if opc==1:
                for i in range(len(nombres)):
                    print('Ciclista '+str(i+1)+': ',nombres[i])
                    for j in range(len(tiempos)):
                        print('E'+str(j+1)+': ',tiempos[j][i])

                for i in range(len(tiempos)):
                    ind=mejor(i,0)
                    print('\nMejor tiempo en la etapa '+str(i+1)+':')
                    print(nombres[ind])
                    while True:
                        ind2=mejor(i,ind+1)
                        if ind==ind2:
                            print(nombres[ind2])
                            ind=ind2
                        else:
                            break
                    
                    inde=peor(i,0)
                    print('\nPeor tiempo en la etapa '+str(i+1)+':')
                    print(nombres[inde])
                    while True:
                        inde2=mejor(i,inde+1)
                        if inde==inde2:
                            print(nombres[inde2])
                            inde=inde2
                        else:
                            break

#            elif opc==2:

#            elif opc==3:

#            elif opc==4:

            elif opc==5:
                break
            else:
                print('<Opción no válida>\n')

#Eliminar
    #elif op==3:

#Modificar
    #elif op==4:

    elif op==5:
        print('Hasta luego :D')
        break
    else:
        print('<Opción no válida>\n')