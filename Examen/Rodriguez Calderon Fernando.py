def innum ():
    #Entrada de numeros
   while True:
      try:
         x=int(input('> '))
         print('')
         break
      except ValueError:
         print('<ERROR: Valor no válido>\n')
   return (x)

def innumtxt(a):
    #Entrada de numeros con un texto elegido 
   while True:
      try:
         x=int(input(a))
         print('')
         break
      except ValueError:
         print('<ERROR: Valor no válido>\n')
   return (x)

def innumfloat(a):
    #Entrada de numeros flotantes con un texto elegido 
   while True:
      try:
         x=float(input(a))
         print('')
         break
      except ValueError:
         print('<ERROR: Valor no válido>\n')
   return (x)

def buscar(x,lista):
    #Busca algo en una lista
    res=-1
    for i in range (len(lista)):
        if x==lista[i]:
            res=i
            break
    return (res)

def registro(n):
    #Registra el nombre del cilcista
    while True:
        nom=str(input('Ingresar el nombre del ciclista con apellido: '))
        if nom.isalpha():
            print('\nLa información esta incompleta o no es válida\n')
        else:
            if ' 'in nom:
                if (nom[0]==' ')or(nom[-1]==' '):
                    print('\nLa información esta incompleta o no es válida\n')
                else:
                    p=nom.replace(' ','')
                    if p.isalpha():
                        p=p.upper()
                        nombres.append(nom.title())
                        conjuntos.append(p)
                        break
                    else:
                        print('\nLa información esta incompleta o no es válida\n')
            else:
                print('\nLa información esta incompleta o no es válida\n')
    
    #Registra los n tiempos del ciclista
    while True:
        for i in range (n):
            x=innumfloat('Ingrese el tiempo en la etapa '+str(i+1)+': ')
            tiempos[i].append(x)
        break
    return()

def mejor(etapa,n):
    #Obtiene al mejor tiempo de una etapa a partir de un indice n
    t=tiempos[etapa].copy()
    mej=t[n]
    indice=n
    for i in range(n+1,len(t)):
        if mej>t[i]:
            mej=t[i]
            indice=i
    return(indice)

def peor(etapa,n):
    #Obtiene al peor tiempo de una etapa a partir de un indice n
    t=tiempos[etapa].copy()
    peor=t[n]
    indice=n
    for i in range(n,len(t)):
        if peor<t[i]:
            peor=t[i]
            indice=i
    return(indice)

def top(d,i):
    #Imprime al mejor(es) o peor(es) de una de las etapas
    if d:
        #mejor
        ind=mejor(i,0)
        print('Mejor tiempo:')
        print(nombres[ind],' ',tiempos[i][ind])
        while True:
            if ind<len(tiempos[i])-1:
                index2=mejor(i,ind+1)
                if tiempos[i][ind]==tiempos[i][index2]:
                    print(nombres[index2],' ',tiempos[i][index2])
                    ind=index2
                else:
                    break
            else:
                break
        print('')

    else:
        #peor
        ind=peor(i,0)
        print('Peor tiempo:')
        print(nombres[ind],' ',tiempos[i][ind])
        while True:
            if ind<len(tiempos[i])-1:
                index2=peor(i,ind+1)
                if tiempos[i][ind]==tiempos[i][index2]:
                    print(nombres[index2],' ',tiempos[i][index2])
                    ind=index2
                else:
                    break
            else:
                break
        print('')
    return()

def primero(n):
    #Obtiene al mejor tiempo de la vuelta a partir de un indice n
    t=vueltas.copy()
    mej=t[n]
    indice=n
    for i in range(n+1,len(t)):
        if mej>t[i]:
            mej=t[i]
            indice=i
    return(indice)

def podio():
    #Obtiene al mejor tiempo de la suma de todas las etapas
    ind=primero(0)
    print('\n    Ganador de la vuelta')
    print('============================')
    print(nombres[ind],' ',vueltas[ind])
    while True:
        if ind<len(vueltas)-1:
            index2=primero(ind+1)
            if vueltas[ind]==vueltas[index2]:
                print(nombres[index2],' ',vueltas[index2])
                ind=index2
            else:
                break
        else:
            break

def printiempos(x):
    #Imprime los tiempos de las distintas etapas de un ciclista con indice x
    for i in range(len(tiempos)):
        print('E'+str(i+1)+': ',tiempos[i][x])
    print('')
    return()

def similitud(a,b):
    #Busca la similitud entre dos conjuntos
    I=[]
    U=[]
    A=[]
    B=[]
    for i in range(len(a)):
        A.append(a[i])
    for i in range(len(b)):
        B.append(b[i])

    for i in range (len(A)):
        if (B.count(A[i])>0)and(I.count(A[i])==0):
            I.append(A[i])
        if U.count(A[i])==0:
            U.append(A[i])

    for i in range (len(B)):
        if U.count(B[i])==0:
            U.append(B[i])

    x=(len(I)/len(U))*100
    return(x)

def confirma(a):
    #Decisión con un mensaje a
    while True:
        print(a)
        d=str(input('S/N: '))
        print('')
        d=d.upper()
        d=d.replace(' ','')
        if d=='S':
            x=True
            break
        elif d=='N':
            x=False
            break
        else:
            print('<Opción no válida>\n')
    return(x)

def cambionomb(x):
    nom_antiguo=nombres[x]
    while True:
        nom=str(input('Ingrese el nuevo nombre del ciclista: '))
        if nom.isalpha():
            print('\nLa información esta incompleta o no es válida\n')
        else:
            if ' 'in nom:
                if (nom[0]==' ')or(nom[-1]==' '):
                    print('\nLa información esta incompleta o no es válida\n')
                else:
                    p=nom.replace(' ','')
                    if p.isalpha():
                        p=p.upper()
                        nombres.pop(x)
                        conjuntos.pop(x)
                        nombres.insert(x,nom.title())
                        conjuntos.insert(x,p)
                        print('\nEl registro ha sido modificado')
                        print(nom_antiguo,'-->',nombres[x])
                        break
                    else:
                        print('\nLa información esta incompleta o no es válida\n')
            else:
                print('\nLa información esta incompleta o no es válida\n')

def nueva_etapa():
    tiempos.append([])
    print('        Una nueva etapa ha sido creada')
    print('==============================================')
    for i in range(len(nombres)):
        x=innumfloat('Introduce el tiempo para '+nombres[i]+' en la etapa '+str(len(tiempos))+': ')
        tiempos[-1].append(x)
    print('-La informaciòn ha sido guardada correctamente-\n')
    return()

nombres=[]
conjuntos=[]
tiempos=[[]]

# A diferencia de lo que pedia el pdf, use la matriz de una manera transpuesta
# en el codigo las filas de la matriz "tiempos" representan las distintas etapas 
# y las columnas a los ciclistas

while True:
    print('\n    Menú Principal')
    print('======================')
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
            #Nùmero de etapas iniciales
            registro(1)
        else:
            registro(len(tiempos))

#Consulta            
    elif op==2:
        if len(nombres)==0:
            print(' ==============================')
            print('| No hay ciclistas registrados |')
            print(' ==============================')
        else:
            while True:
                print('    Menú de consulta')
                print('========================')
                print('1) Consultar todo')
                print('2) Consultar tiempos por ciclista')
                print('3) Ganador por etapa')
                print('4) Ganador de la vuelta')
                print('5) Regresar al menú principal\n')
                print('Escoja una opción')
                opc=innum()

            #Consultar todo
                if opc==1:
                    print('           Ciclistas')
                    print('==============================')
                    for i in range(len(nombres)):
                        print(nombres[i])
                        printiempos(i) 

                    for i in range(len(tiempos)):
                        print('           Etapa: ',str(i+1))
                        print('==============================')
                        top(True,i)
                        top(False,i) 
                        print('')   
                    break
                
            #Consultar tiempos por ciclista
                elif opc==2:
                    nom_bus=str(input('Introduzca el nombre del ciclista: '))
                    nom_bus=nom_bus.upper()
                    nom_bus=nom_bus.replace(' ','')
                    pos=buscar(nom_bus,conjuntos)

                    if pos==-1:
                        orden=[]
                        simi=[]
                        for i in range (len(conjuntos)):
                            n=similitud(nom_bus,conjuntos[i])
                            simi.append(n)
                        sim=simi.copy()

                        while len(sim)>0:
                            x=(sim.index(max(sim)))
                            #El numero es el límite para decir que son similares
                            #menos de 40% no se considerará similar
                            if sim[x]>40:
                                orden.append(x)
                            sim.pop(x)

                        if len(orden)>0:
                            print('No se encontro al ciclista, tal vez quisiste decir:\n')
                            for i in (orden):
                                print(nombres[i],f'{simi[i]/100:.2%}','de coincidencia')
                                print('Los tiempos registrados son:')
                                printiempos(i)
                            break
                        else:
                            print('No se encontraron resultados similares\n')

                    else:
                        print('Los tiempos registrados de',nombres[pos],'son:')
                        printiempos(pos)
                        break

            #Ganador por etapa
                elif opc==3:
                    while True:
                        x=innumtxt('Introduzca el número de la etapa a consultar: ')
                        if x>len(tiempos):
                            print('No hay registros de una etapa',x)
                            print('Por favor introduzca una etapa válida\n')
                        else:
                            break
                    
                    print('       Ganador etapa: ',str(i+1))
                    print('==============================')
                    top(True,x-1)
                    break
                
            #Ganador de la vuelta            
                elif opc==4:
                    vueltas=[]
                    for i in range(len(nombres)):
                        sum=0
                        for j in range(len (tiempos)):
                            sum+=tiempos[j][i]
                        vueltas.append(sum)

                    podio()
                    break             

            #Regresar al menu principal
                elif opc==5:
                    break
                else:
                    print('<Opción no válida>\n')

#Eliminar
    elif op==3:
        if len(nombres)==0:
            print(' ==============================')
            print('| No hay ciclistas registrados |')
            print(' ==============================')
        else:
            while True:
                print('    Menú eliminar')
                print('=====================')
                print('1) Eliminar etapa')
                print('2) Eliminar ciclista')
                print('3) Regresar al menú principal\n')
                print('Escoja una opción')
                ope=innum()

            #Eliminar etapa
                if ope==1:
                    if len(tiempos)==1:
                        print('Solo hay una etapa registrada, no es posible eliminarla\n')

                    else:
                        while True:
                            x=innumtxt('Introduzca el número de la etapa que desea eliminar: ')
                            if x>len(tiempos):
                                print('No hay registros de una etapa',x)
                                print('Por favor introduzca una etapa válida\n')
                            else:
                                break 

                        if confirma('¿Esta seguro que desea eliminar la etapa '+str(x)+'?'):
                            tiempos.pop(x-1)
                            print('La etapa '+str(x),'ha sido eliminada de los registros')
                        
                        break

            #Eliminar ciclista
                elif ope==2:
                    nom_bus=str(input('Introduzca el nombre del ciclista: '))
                    nomb=nom_bus.title()
                    nom_bus=nom_bus.upper()
                    nom_bus=nom_bus.replace(' ','')
                    pos=buscar(nom_bus,conjuntos)

                    if pos==-1:
                        simi=[]
                        for i in range (len(conjuntos)):
                            n=similitud(nom_bus,conjuntos[i])
                            simi.append(n)

                        x=simi.index(max(simi))
                        print('No se encontro al ciclista '+nomb+',','tal vez quisiste decir:',nombres[x])

                        if confirma('¿Desea eliminar sus registros?'):
                            print(nombres[x],'ha sido removido de los registros')
                            nombres.pop(x)
                            for i in range(len(tiempos)):
                                tiempos[i].pop(x)
                            break

                    else:
                        if confirma('¿Esta seguro que desea eliminar los registros de: '+nombres[pos]+'?'):
                            print(nombres[pos],'ha sido removido de los registros')
                            nombres.pop(pos)
                            for i in range(len(tiempos)):
                                tiempos[i].pop(pos)
                            break

            #Regresar al menú principal
                elif ope==3:
                    break

                else:
                    print('<Opción no válida>\n')

#Modificar
    elif op==4:
        if len(nombres)==0:
            print(' ==============================')
            print('| No hay ciclistas registrados |')
            print(' ==============================')
        else:
            while True:
                print('    Menú modificar')
                print('======================')
                print('1) Modificar nombre de ciclista')
                print('2) Modificar tiempo de etapa')
                print('3) Agregar nueva etapa')
                print('4) Ordenar alfabéticamente')
                print('5) Regresar al menú principal\n')
                print('Escoja una opción')
                opm=innum()

            #Modificar nombre de ciclista
                if opm==1:
                    nom_bus=str(input('Introduzca el nombre del ciclista: '))
                    nomb=nom_bus.title()
                    nom_bus=nom_bus.upper()
                    nom_bus=nom_bus.replace(' ','')
                    pos=buscar(nom_bus,conjuntos)

                    if pos==-1:
                        simi=[]
                        for i in range (len(conjuntos)):
                            n=similitud(nom_bus,conjuntos[i])
                            simi.append(n)

                        x=simi.index(max(simi))
                        print('No se encontro al ciclista '+nomb+',','tal vez quisiste decir:',nombres[x])

                        if confirma('¿Desea modificar el nombre?'):
                            cambionomb(x)
                            break

                    else:
                        cambionomb(pos)
                        break

            #Modificar tiempo de etapa
                elif opm==2:
                    nom_bus=str(input('Introduzca el nombre del ciclista: '))
                    nomb=nom_bus.title()
                    nom_bus=nom_bus.upper()
                    nom_bus=nom_bus.replace(' ','')
                    pos=buscar(nom_bus,conjuntos)

                    if pos==-1:
                        simi=[]
                        for i in range (len(conjuntos)):
                            n=similitud(nom_bus,conjuntos[i])
                            simi.append(n)

                        x=simi.index(max(simi))
                        print('No se encontro al ciclista '+nomb+',','tal vez quisiste decir:',nombres[x])

                        if confirma('¿Desea modificar los tiempos?'):
                            while True:                
                                et=innumtxt('Introduzca el nùmero de etapa a modificar: ')
                                if et>len(tiempos):
                                    print('No hay registros de una etapa',et)
                                    print('Por favor introduzca una etapa válida\n')
                                else:
                                    break 
                            
                            tiempo_antiguo=tiempos[et-1][x]
                            print('Tiempo registrado:\n','E'+str(et)+':',tiempo_antiguo)
                            tiempo_nuevo=innumfloat('Introduzca el nuevo tiempo: ')
                            tiempos[et-1].pop(x)
                            tiempos[et-1].insert(x,tiempo_nuevo)
                            print('Se han modificado los registros')
                            print('E'+str(et)+':',tiempo_antiguo, '-->',tiempo_nuevo)
                            break

                    else:
                        while True:                
                            et=innumtxt('Introduzca el nùmero de etapa a modificar: ')
                            if et>len(tiempos):
                                print('No hay registros de una etapa',et)
                                print('Por favor introduzca una etapa válida\n')
                            else:
                                break 

                        tiempo_antiguo=tiempos[et-1][pos]
                        print('Tiempo registrado:\n','E'+str(et)+':',tiempo_antiguo)
                        tiempo_nuevo=innumfloat('Introduzca el nuevo tiempo: ')
                        tiempos[et-1].pop(pos)
                        tiempos[et-1].insert(pos,tiempo_nuevo)
                        print('Se han modificado los registros')
                        print('E'+str(et)+':',tiempo_antiguo, '-->',tiempo_nuevo)
                        break

            #Agergar nueva etapa
                elif opm==3:
                    if confirma('¿Desea agregar una nueva etapa?'):
                        nueva_etapa()
                        break

            #Ordenar por orden alfabético
                elif opm==4:
                    if confirma('¿Desea organizar la informaciòn alfabéticamente?'):
                        nombres_orden=nombres.copy()
                        tiempos_orden=[]
                        conjuntos_orden=[]
                        
                        orden=[]

                        while len(nombres_orden)>0:
                            x=nombres_orden.index(min(nombres_orden))
                            orden.append(x)
                            nombres_orden.pop(x)

                        nombres.sort()

                        for i in (orden):
                            conjuntos_orden.append(conjuntos[i])
                        conjuntos=conjuntos_orden

                        for i in range (len(tiempos)):
                            l=[]
                            for j in (orden):
                                l.append(tiempos[i][j])
                            tiempos_orden.append(l)
                        tiempos=tiempos_orden

                        print('-La informaciòn se ha organizado correctamente-\n')
                        break

            #Regresar
                elif opm==5:
                    break
                else:
                    print('<Opciòn no vàlida>\n')

#Salir
    elif op==5:
        print('Hasta luego :D\n')
        break
    
    else:
        print('<Opción no válida>\n')

#Jaja
#saludos
#Cutli es pvto