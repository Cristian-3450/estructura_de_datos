import pickle #importa la biblioteca necesaria

#creo la variable archivo
with open('ejemplo.pkl','wb') as archivo: #crea un punto de accceso a los datos a partir del archivo
    pkl=pickle.Pickler(archivo)
    
    lista1=[1,2,3]
    lista2=[4,5]
    diccionario={'campo1':1,'campo2':'dos'}
    
    pkl.dump(lista1)
    pkl.dump(None)
    pkl.dump(lista2)
    pkl.dump('Hola Mundo')
    pkl.dump(diccionario)
    pkl.dump(1)

# with open('ejemplo.pkl','wb') as archivo:
#     seguir_leyendo=True
#     while seguir_leyendo:
#
lista=[
    {'usuario':'usuario1','puntaje':5},
    {'usuario':'usuario2','puntaje':3},
    {'usuario':'usuario3','puntaje':1},
]

with open('ejemplo2.pkl','wb')as archivo:
    pkl=pickle.Pickler(archivo)
    pkl.dump(lista)
    
with open('ejemplo2.pkl','rb')as archivo:
    data=pickle.load(archivo)
    print(data)
    