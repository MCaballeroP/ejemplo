import tabulate
# -*- coding: utf-8 -*-

#crear datos en un archivo csv

#abrir archiuvo (nombre+extencion)
#modod de apertura W,r,a,b(write, read, adition, binario)
file=open('datos.csv','w')

#escribir datos
#file.write("hola, este es mi primer archivo")
equipo = "ompresora ed;general electric;30;2022-08-20"
equipo2 = "sensor cardiaco;xxxx;10;15;2022-07-30"
file.write(equipo + '\n')
file.write(equipo2 + '\n')
#cerrar archivo
file.close()

#modo adicion
file=open('datos.csv','a')
equipo = "multimetro;general electric;30;2022-08-20"
file.write(equipo + '\n')
file.close()


#modo leer archivo

archivo =open('datos.csv','r')
lineas =archivo.readlines()
header = ["Nombre", "Proveedor", "cantidad", "Ciclo", "FUM" ]

datos=[]
datos.append(lineas)
for l in lineas:
    l= l.replace("\n","")
    l =l.split(";")
    datos.append(l)
    
print=(tabulate(datos, header, tablefmt="grid"))