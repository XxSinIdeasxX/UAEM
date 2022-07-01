
#El codigo no lee los valores ni los escribe, linea 43 y 63

alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros='01234567890123456789'
proceso=True

def innum ():
   while True:
      try:
         print('\nIntroduzca la clave de encriptación')
         x=int(input())
         break
      except ValueError:
         print('<ERROR: VALOR NO VÁLIDO>')
   return (x)

def leeropcion():
   while True:
      try:
         x=str(input())
         x=x.upper()
         if not((x=='A')or(x=='B')):
            print('<Opcion no válida>')
         else:
            break
      except ValueError:
         print('<ERROR: VALOR NO VÁLIDO>')
   return(x)

def inmensaje ():
   while True:
      try:
         print('\nElija una opción:\n','a) Escribir un mensaje\n','b) Leer un mensaje de un archivo .txt')
         op=leeropcion()
         if op=='A':
            print('Introduzca el mensaje:')
            x=str(input())
            break
         elif op=='B':
            print('Introduzca el nombre del arhivo (incluya la terminación .txt)')
            arch=str(input())
            archivo = open(arch, 'r') 
            x=archivo.read() 
            print(x)
            archivo.close()
            break
      except ValueError:
         print('<ERROR: VALOR NO VÁLIDO>')
   return(x)

def imprimir(men):
   print('¿Desea guardar el texto en un archivo .txt?')
   while True:
      print('S/N')
      x=input()
      x=x.upper()
      if not((x=='S')or(x=='N')):
         print('<Opción no válida')
      else:
         if x=='S':
            archivo = open('mensaje.txt', 'w') 
            archivo.write(men) 
            archivo.close()
            print('\nEl mensaje se ha estrito en el archivo mensaje.txt\n')
         else:
            print('\nEsta bien :P\n')   
         break
   return()
   


while proceso:
   enc=''
   print('Escoja una opcion\n','a) Encriptar un mensaje\n','b) Desencriptar un mensaje\n','c) Salir')
   opcion=input()

   if opcion=='a':
      N=innum()
      while(N>=27):
         N-=27
      mensaje=inmensaje()

      mensaje=mensaje.upper()
      mensaje=mensaje.replace('Á','A')
      mensaje=mensaje.replace('É','E')
      mensaje=mensaje.replace('Í','I')
      mensaje=mensaje.replace('Ó','O')
      mensaje=mensaje.replace('Ú','U')

      for i in range(len(mensaje)):
         if mensaje[i]==' ':
            enc+=' '
         elif mensaje[i]==',':
            enc+=','
         elif mensaje[i]=='.':
            enc+='.'
         for x in range(10):
               if mensaje[i]==numeros[x]:
                  enc+=numeros[x+N]

         for x in range(27):
               if mensaje[i]==alpha[x]:
                  enc+=alpha[x+N]
      print('\n>>>',enc,'\n')
      imprimir(enc)
      
   elif opcion=='b':
      N=innum()
      while(N>=27):
         N-=27
      mensaje=inmensaje()

      mensaje=mensaje.upper()
      mensaje=mensaje.replace('Á','A')
      mensaje=mensaje.replace('É','E')
      mensaje=mensaje.replace('Í','I')
      mensaje=mensaje.replace('Ó','O')
      mensaje=mensaje.replace('Ú','U')

      for i in range(len(mensaje)):
         if mensaje[i]==' ':
            enc+=' '
         elif mensaje[i]==',':
            enc+=','
         elif mensaje[i]=='.':
            enc+='.'
         for x in range(len(numeros)/2,len(numeros)):
               if mensaje[i]==numeros[x]:
                  enc+=numeros[x-N]

         for x in range(len(alpha)/2,len(alpha)):
               if mensaje[i]==alpha[x]:
                  enc+=alpha[x-N]

      print('\n>>>',enc,'\n')
      imprimir(enc)

   elif opcion=='c':
      print('Gracias por utilizar el programa :D')
      break
   else:
      print('<ERROR: OPCIÓN NO VÁLIDA>\n')
