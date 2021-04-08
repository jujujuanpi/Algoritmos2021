# Búsqueda Lineal

def busquedaLineal(lista,encontrar):
    isInList = False
    for elemento in lista:
        if elemento == encontrar:
            isInList = True
    return isInList

listaEntrada = [2,12,34,5,11,59,4,3,1]
valorEntrada = int (input("Ingresar un número: "))

print (busquedaLineal(listaEntrada, valorEntrada))

import busquedabinaria as bi
import time

encontrar = 59

inicio = time.time()
busquedaLineal(listaEntrada, encontrar)
deltaLineal = time.time() - inicio

inicio = time.time()
bi.busquedaBinaria(listaEntrada,encontrar)
deltaBinaria = time.time() - inicio

print (deltaLineal,deltaBinaria) # Binaria será más corta, ha que eliminar todos los prints y la lista del final del código binario.