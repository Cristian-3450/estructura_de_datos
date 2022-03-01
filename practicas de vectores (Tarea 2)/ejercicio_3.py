class Promedio:
    def hallar_promedio(self):
        a=[4,5,9,7,8,30]
        suma=0
        prom=0
        for i in a:
            suma=suma+i
        prom=suma/len(a)
        print("El promedio del vector es: "+str(prom))
promedio=Promedio()
promedio.hallar_promedio()