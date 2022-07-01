print('Introduzca la palabra:')
pal=input()
p=pal.lower()
p=p.replace(' ','')
p=p.replace(',','')
p=p.replace('á','a')
p=p.replace('é','e')
p=p.replace('í','i')
p=p.replace('ó','o')
p=p.replace('ú','u')
inv=''
for i in range (len(p)):
   inv+=p[len(p)-1-i]
if (p==inv):
   print(pal, ' es palindromo')
else:
   print(pal, ' no es palindormo')
