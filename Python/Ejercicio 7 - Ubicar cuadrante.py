print('Introduce las coordenadas x:')
x=float(input())
print('Introduce las coordenadas y:')
y=float(input())
if x*y<0:
   if x<0:
      c='segundo'
   else:
      c='cuarto'
else:
   if x<0:
      c='tercer'
   else:
      c='primer'
print('El punto esta en el ',c,' cuadrante')
