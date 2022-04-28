import os

print ("\nCrear un archivo")
print ("================")

NOMBRE_ARCHIVO = 'datos_1.txt'

archivo = open(NOMBRE_ARCHIVO, 'w') # abre el archivo datos.txt
archivo.write('Paquete 1\n')
archivo.write('4-5 personas \t 450$ \t 3 dias \t alojamiento,comida,transporte (solo a lugares turisticos)\n\n')
archivo.write('Paquete 2\n')
archivo.write('2-3 personas \t 500$ \t 5 dias \t alojamiento,comida,transporte (solo a lugares turisticos),guia\n\n')
archivo.write('Paquete 3\n')
archivo.write('5-6 personas \t 1000$ \t 10 dias \t alojamiento,comida,transporte (solo a lugares turisticos),guia y traductor\n\n')
archivo.write('Paquete 4\n')
archivo.write('2-4 personas \t 650$ \t 6 dias \t alojamiento,comida,transporte (solo a lugares turisticos),guia\n\n')
archivo.write('Paquete 5\n')
archivo.write('5-6 personas \t 1100$ \t 6 dias \t alojamiento,comida,transporte (solo a lugares turisticos),guia y traductor\n\n')
archivo.close()

if NOMBRE_ARCHIVO in os.listdir("."):
    print("\nArchivo creado en la ruta: \n\n\t{0}/t{1}".format(os.getcwd(),NOMBRE_ARCHIVO))
else:
    print("El archivo no fue creado!!!!!!\n")