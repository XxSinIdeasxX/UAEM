print('Introduzca cinco números')
pos=0
for x in range(0,5):
   num=int(input())
   if num>0:
      pos+=1
print(pos,' números son positivos')
