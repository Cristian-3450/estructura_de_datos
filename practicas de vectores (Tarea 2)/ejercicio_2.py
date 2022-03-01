class Minimo:
    def hallar_minimo(self):
        a=[4,5,-9,7,1,30]
        min=a[0]
        for i in a:
            if i<min:
                min=i
        print("El numero minimo es: "+str(min))
minimo=Minimo()
minimo.hallar_minimo()