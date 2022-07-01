def innum ():
   while True:
      try:
         x=int(input('>>> '))
         break
      except ValueError:
         print('<ERROR: CARACTER NO VÁLIDO>')
   return (x)

def llenado (conjunto,n):
    print('\nIntroduzca el valor de los elementos del conjunto')
    for i in range(n):
        conjunto.append(innum())
    return

A=[]
B=[]
U=[]
I=[]

print('\nIntroduzca el número de elementos del primer conjunto')
n=innum()
llenado(A,n)

print('\nIntroduzca el número de elementos del segundo conjunto')
m=innum()
llenado(B,m)

for i in range (len(A)):
    if (B.count(A[i])>0)and(I.count(A[i])==0):
        I.append(A[i])
    if U.count(A[i])==0:
        U.append(A[i])

for i in range (len(B)):
    if U.count(B[i])==0:
        U.append(B[i])
I.sort()
U.sort()
print('\nConjunto 1:  ',A)
print('Conjunto 2:  ',B)
print('Intersección:',I)
print('Unión:       ',U)