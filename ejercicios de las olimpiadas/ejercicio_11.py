#!/usr/bin/env python
#-*-coding:utf-8-*-

# def inversa(cadena):
#     invertida=""
#     cont=len(cadena)
#     indice=-1
#     while cont>=1:
#          invertida+=cadena[indice]
#          indice=indice+(-1)
#          cont-=1
#     return invertida
def es_palindromo(cadena):
     if cadena==cadena[::-1]:
           
           #print("Es palindromo")
           return True
     else:
           #print("No es palindromo")
           return False
palabra=input("Introduce una palabra: ")
if es_palindromo(palabra)==True:
    print("Es palindromo")
else:
    print("No es palindromo")
          
