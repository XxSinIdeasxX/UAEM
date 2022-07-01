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
    return(M)

def creacion(m,n):
    M=[]
    for i in range(m):
        l=[0]*n
        M.append(l)
    return(M)

A=[]
B=[]
C=[]

print('Introduce el número de columnas de las matrices')
n=innum()
print('\nIntrodue el número de filas de las matrices')
m=innum()

print('\nIntroduce los valores de la primera matriz')
A=llenado(m,n)

print('\nIntroduce los valores de la segunda matriz')
B=llenado(m,n)

C=creacion(m,n)

for j in range(m):
    for i in range(n):
        C[j][i]=A[j][i]+B[j][i]

for i in range(m):
    print(A[i],' ',B[i],' ',C[i])