class revertir_lista:
    def revertidor(self):
        from array import array
        numeros = array('i',[2,3,4,5,6,7])
        print(numeros)
        print()
        numeros.reverse()
        print(numeros)
revertir=revertir_lista()
revertir.revertidor()