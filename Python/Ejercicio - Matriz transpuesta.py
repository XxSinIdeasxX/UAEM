def innum ():
   while True:
      try:
         x=int(input('> '))
         break
      except ValueError:
         print('<ERROR: VALOR NO VÁLIDO>')
   return (x)

def llenado(m,n):
    l=[]
    M=[]
    for j in range(m):
        l=[]
        for i in range (n):
            x=innum()
            l.append(x)
        M.append(l)

    print('')

    for u in range(m):
        print(M[u])
    return(M)

def creacion(m,n):
    M=[]
    for i in range(n):
        l=[0]*m
        M.append(l)
    return(M)

M=[]
T=[]

print('\nIntroduce el número de columnas de la matriz')
n=innum()

print('Introduce el numero de filas de la matriz')
m=innum()

print('\nIntroduce los valores de la matriz')
M=llenado(m,n)
T=creacion(m,n)

for j in range(m):
    for i in range(n):
        T[i][j]=M[j][i]

print('')

for u in range(n):
    print(T[u])
