def innum(a):
    #Entrada de numeros con un texto elegido 
   while True:
      try:
         x=int(input(a))
         break
      except ValueError:
         print('<ERROR: Valor no válido>\n')
   return (x)

def imp(M):
    for i in range(len(M)):
        print(M[i])

M=[]
a=[]

m=innum('Ingrese el número de filas: ')
n=innum('Ingrese el número de columnas: ')
print('')
for i in range(m):
    l=[]
    for j in range(n):
        x=innum('> ')
        a.append(x)
        l.append(x)
    M.append(l)

print('\nMatriz original')
imp(M)

b=[]

while len(a)>0:
    men=a[0]
    indice=0
    for i in range(len(a)):
        if men>a[i]:
            men=a[i]
            indice=i
    b.append(men)
    a.pop(indice)

k=0
for i in range(m):
    for j in range(n):
        M[i][j]=b[k]
        k+=1
print('\nMatriz ordenada')
imp(M)