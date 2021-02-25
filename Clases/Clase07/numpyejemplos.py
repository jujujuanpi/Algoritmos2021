import numpy as np

lista = [5,9,4,6]

listaC = []
for i in range (200,800,2):
    listaC.append(i)
print (listaC)

listaN = np.arange (200,801,2)
print (listaN)
print (listaN[:101])

listaNu = np.arange (1,11,1)
listaNu[::2] = 200
print (listaNu)

#------------ Indexación Lógica ------------#

edades = [14,23,34,56,11,8,23]
edades = np.array (edades)

indiceEdades = edades > 18

print (edades)
print (indiceEdades)

totalMayorEdad = np.sum(indiceEdades)
print (totalMayorEdad)

# Arange se usa cuando se crea la lista en un intervalo, y Array se usa cuando a partir de una lista creada se hace un arreglo.

indiceEdades2 = edades == 23
indiceEdades3 = edades == 56
indiceEdades4 = indiceEdades2 | indiceEdades3

# | significa o, siendo una u otra cosa.

print (indiceEdades2)
print (indiceEdades3)
print (indiceEdades4)

totalEjemplo = np.sum(indiceEdades4)
print (totalEjemplo)

# Listado en un intervalo desde algo que existe

indiceEdadesInt1 = edades >= 23
indiceEdadesInt2 = edades <= 50
indiceEdadesInt = indiceEdadesInt1 & indiceEdadesInt2

# & es el y, siendo una cosa y otra.

totalInt = np.sum(indiceEdadesInt)
print (totalInt)

# Promedio Numpy

print (np.mean (edades))

#------------ Mamás ------------#
print ('#'*30)
mamas = [58,58,95,64,74,43,55]
mamas = np.array (mamas)

hijosMayores30 = edades > 30
print (hijosMayores30)

#------------ Matriz Numpy ------------#
print ('#'*30)
edadesHijos = np.array([14,18,22,24])
edadesMamas = np.array ([44,48,51,52])

kidsMoms = np.array ([edadesHijos, edadesMamas])

print (kidsMoms)

# Transponer Matrices
print (kidsMoms.transpose())
print ('#'*30)

indiceKids = kidsMoms[0] >= 18
print (indiceKids)
print (np.sum(indiceKids))
print ('#'*30)
print (kidsMoms[1][indiceKids])
print (np.mean(kidsMoms[1][indiceKids]))
print (len(kidsMoms[1][indiceKids]))