class Capicua:
    def probar_capicua(self):
        a=[4,5,9,7,8,30]
        b=list(reversed(a))
        print("vector a: ")
        print(a)
        print("vector b: ")
        print(b)
        if a==b:
            print("El vector a es capicua")
        else:
            print("El vector a no es capicua")
capicua=Capicua()
capicua.probar_capicua()