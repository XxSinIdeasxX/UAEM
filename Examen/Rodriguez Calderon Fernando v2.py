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
            print('\nLa información no esta completa o no es válida\n')
        else:
            if ' 'in nom:
                p=nom.replace(' ','')
                if p.isalpha():
                    p=p.upper()
                    nombres.append(nom.title())
                    conjuntos.append(p)
                    break
                else:
                    print('\nLa información no esta completa o no es válida\n')
            else:
                print('\nLa información no esta completa o no es válida\n')
    
    #Registra los n tiempos del ciclista
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
        print('\nMejor tiempo en la etapa '+str(i+1)+':')
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
    else:
        #peor
        ind=peor(i,0)
        print('\nPeor tiempo en la etapa '+str(i+1)+':')
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
    return()

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

nombres=[]
conjuntos=[]
tiempos=[[]]

while True:
    print('\n  Menu Principal')
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
            print('    Menu de consulta')
            print('========================')
            print('1) Consultar todo')
            print('2) Consultar tiempos por ciclista')
            print('3) Ganador por etapa')
            print('4) Ganador de la vuelta')
            print('5) Regresar al menu principal\n')
            print('Escoja una opción')
            opc=innum()
            
        #Consultar todo
            if opc==1:
                print('==============================')
                for i in range(len(nombres)):
                    print('Ciclista '+str(i+1)+': ',nombres[i])
                    printiempos(i) 

                for i in range(len(tiempos)):
                    print('==============================')
                    top(True,i)
                    top(False,i)    
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
                        print(simi)
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
                    try:
                        x=int(input('Introduzca el número de la etapa a consultar: '))
                        print('')
                        if x>len(tiempos):
                            print('No hay registros de una etapa',x)
                            print('Por favor introduzca una etapa válida\n')
                        else:
                            break
                    except ValueError:
                        print('<ERROR: Valor no válido>\n')
                
                top(True,x-1)
                break
            
        #Ganador de la vuelta            
        #    elif opc==4:
        
        #Regresar al menu principal
            elif opc==5:
                break
            else:
                print('<Opción no válida>\n')

#Eliminar
    #elif op==3:

#Modificar
    #elif op==4:

#Salir
    elif op==5:
        print('Hasta luego :D')
        break
    
#Omisión
    else:
        print('<Opción no válida>\n')