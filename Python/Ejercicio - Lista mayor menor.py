N=int(input('Introduce la longitud de la lista \n'))
l=[]
print('Introduce los números')
for i in range(N):
   n=int(input())
   l.append(n)
may=l[0]
men=l[0]
for i in range(1,len(l)):
   if may<=l[i]:
      may=l[i]
   elif men>=l[i]:
      men=l[i]
print('El número mayor es: ',may,' y el menor es: ', men)
