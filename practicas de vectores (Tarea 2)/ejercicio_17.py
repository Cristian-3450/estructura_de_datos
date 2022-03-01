class Generar_f:
    def generador(self):
        a=[]
        limite=int(input("Ingrese cuantos numeros desea ver de la secuencia: "))
        b=0
        c=1
        d=0
        for i in range(limite):
            d=b+c
            a.append(d)
            b=c
            c=d 
        print(a)
generar=Generar_f()
generar.generador()

            
            