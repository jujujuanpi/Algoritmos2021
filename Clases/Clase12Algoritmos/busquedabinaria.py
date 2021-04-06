# Primero organiza de menor a mayor y luego busca. Usa un valor medio.

def busquedaBinaria (lista, encontrar):
    '''Búsqueda Binaria
        se ingresa una lista y un valor a encontrar
        y devuelve si lo encontró o no.
    '''
    lista.sort()
    isInList = False
    izq = 0
    der = len(lista) - 1
    while izq <= der and isInList == False:
        print (lista)
        medio = (izq+der)//2
        print ("Cálculo medio", (izq+der)//2)
        print (f"Valor izquierda {izq}, Valor medio {medio}, Valor derecha {der}")
        if lista [medio] == encontrar:
            isInList = True
        elif lista [medio] > encontrar:
            der = medio - 1
        else:
            izq = medio + 1
    return isInList

listaEntrada = [2,12,34,5,11,59,4,3,1]
valorEntrada = int (input("Ingresar un número: "))

print (busquedaBinaria(listaEntrada, valorEntrada))