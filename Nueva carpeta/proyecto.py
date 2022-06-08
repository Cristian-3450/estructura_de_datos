import os

def crear_administrador(self):
    NOMBRE_ARCHIVO='administrador.txt'
    administrador=open(NOMBRE_ARCHIVO,'a')
    nombre=input("ingrese un nombre de usuario: ")
    contraseña=input("ingrese su contraseña: ")
    administrador.write(nombre)
    administrador.write("\t")
    administrador.write(contraseña)
    administrador.write("\n")
    administrador.close()
    
def crear_usuario(self):
    NOMBRE_ARCHIVO='usuario.txt'
    usuario=open(NOMBRE_ARCHIVO,'a')
    nombre=input("ingrese un nombre de usuario: ")
    contraseña=input("ingrese su contraseña: ")
    usuario.write(nombre)
    usuario.write("\t")
    usuario.write(contraseña)
    usuario.write("\n")
    usuario.close
def escoger_genero(self):
    NOMBRE_ARCHIVO='genero.txt'
    genero=open(NOMBRE_ARCHIVO,'r')
    g=genero.read()
    print(g)
    genero.close()
    
def elige_idioma(self):
    NOMBRE_ARCHIVO='idioma.txt'
    idioma=open(NOMBRE_ARCHIVO,'r')
    i=idioma.read()
    print(i)
    idioma.close()
def ver_imagenes(self):
    NOMBRE_ARCHIVO='imagenes.txt'
    imagenes=open(NOMBRE_ARCHIVO,'w')
    imagenes.write('Imagenes')
    imagenes.close()
def crear_paquete(self):
    NOMBRE_ARCHIVO='paquete.txt'
    paquete=open(NOMBRE_ARCHIVO,'w')
    paquete.write('Paquete')
    paquete.close()
def elige_lugar(self):
    NOMBRE_ARCHIVO='lugar.txt'
    lugar=open(NOMBRE_ARCHIVO,'r')
    l=lugar.read()
    print(l)
    lugar.close()
def elige_estadia(self):
    NOMBRE_ARCHIVO='estadia.txt'
    estadia=open(NOMBRE_ARCHIVO,'r')
    e=estadia.read()
    print(e)
    estadia.close()
def elige_transporte(self):
    NOMBRE_ARCHIVO='transporte.txt'
    transporte=open(NOMBRE_ARCHIVO,'w')
    transporte.write('Transporte')
    transporte.close()
def efectua_transaccion(self):
    NOMBRE_ARCHIVO='transaccion.txt'
    transaccion=open(NOMBRE_ARCHIVO,'w')
    transaccion.write('Transaccion')
    transaccion.close()
def guardar_factura(self):
    NOMBRE_ARCHIVO='factura.txt'
    factura=open(NOMBRE_ARCHIVO,'w')
    factura.write('Factura')
    factura.close()
def crear_balance(self):
    NOMBRE_ARCHIVO='balance.txt'
    balance=open(NOMBRE_ARCHIVO,'w')
    balance.write('Balance')
    balance.close()


self=[]
op =''
while op!='f':
    print("1.  Registrarse")
    print("2.  Elejir un idioma")
    print("3.  Ver imagenes")
    print("4.  Escoger un paquete")
    print("5.  Escoger lugar de destino")
    print("6.  Seleccionar estadia")
    print("7.  Opciones de transporte")
    print("8. Efectue transaccion")
    print("9. Factura")
    print("10. Mostar balance(solo para administradores)")
    print("f. FIN")
    op=input("Ingrese una opcion: ")

    if op=="1":
        op=3
        while op!="2" and op!="1":
            print("1.  Registrarse como Administrador")
            print("2.  Registrarse como Usuario")
            op=input("ingrese una opcion: ")
            if op=="1":
                 crear_administrador(self)
                 administrador=open("administrador.txt","r")
                 contenido=administrador.read()
                 print(contenido)
                 administrador.close()
            elif op =="2":
                crear_usuario(self)
                usuario=open("usuario.txt","r")
                contenido=usuario.read()
                print(contenido)
                usuario.close()
            else:
                print("ingrese una opcion valida")
    elif op=="2":
        elige_idioma(self)
        idioma=open("idioma.txt","r")
        contenido=idioma.read()
        print(contenido)
        idioma.close()
    elif op=="3":
        ver_imagenes(self)
        imagenes=open("imagenes.txt","r")
        contenido=imagenes.read()
        print(contenido)
        imagenes.close()
    elif op=="4":
        crear_paquete(self)
        paquete=open("paquete.txt","r")
        contenido=paquete.read()
        print(contenido)
        paquete.close()
    elif op=="5":
        elige_lugar(self)
        lugar=open("lugar.txt","r")
        contenido=lugar.read()
        print(contenido)
        lugar.close()
    elif op=="6":
        elige_estadia(self)
    elif op=="7":
        elige_transporte(self)
        transporte=open("transporte.txt","r")
        contenido=transporte.read()
        print(contenido)
        transporte.close()
    elif op=="8":
        efectua_transaccion(self)
        transaccion=open("transaccion.txt","r")
        contenido=transaccion.read()
        print(contenido)
        transaccion.close()
    elif op=="9":
        guardar_factura(self)
#         escoger_genero(self) falta un menu
        factura=open("factura.txt","r")
        contenido=factura.read()
        print(contenido)
        factura.close()
    elif op=="10":
        crear_balance(self)
        balance=open("balance.txt","r")
        contenido=balance.read()
        print(contenido)
        balance.close()
    elif op=="f":
        print("FIN")