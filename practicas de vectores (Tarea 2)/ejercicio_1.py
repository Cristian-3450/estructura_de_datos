class Maximo:
    def hallar_maximo(self):
        a=[4,5,9,7,8,30]
        max=a[0]
        for i in a:
            if i>max:
                max=i
        print("El numero maximo es: "+str(max))
maximo=Maximo()
maximo.hallar_maximo()
