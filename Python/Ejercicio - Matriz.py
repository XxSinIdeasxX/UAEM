def innum ():
   while True:
      try:
         x=int(input('>>> '))
         break
      except ValueError:
         print('<ERROR: VALOR NO VÁLIDO>')
   return (x)

m=[]

print('Introduce el número de filas y columnas de la martiz')
n=innum()
for i in range(0,n):
    a=[0]*n
    a[i]=1
    m.append(a)
    print(m[i])