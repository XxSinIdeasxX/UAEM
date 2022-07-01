from math import *
sup=0
suim=0
for x in range(1,201):
   if fmod(x,2)==0:
      sup+=x
   else:
      suim+=x
print('La súma de los números pares es: ',sup)
print('La súma de los números impares es: ',suim)
