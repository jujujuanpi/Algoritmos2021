import time
import ordenamientoBurbuja as ob
import random as r

lista = []

for i in range (1200):
    lista.append (r.randint(1,10000))

listaCopy = lista.copy()

# ----- Ordenamiento Burbuja ----- #

# Inicio
inicio = time.time() # Tiempo actual

# Instrucciones
ob.orderBubble(lista)

# Delta
deltaOrderBubble = time.time() - inicio

# ----- Ordenamiento Sort ----- #

# Inicio
initial = time.time()

# Instrucciones
listaCopy.sort()

# Delta
deltaSort = time.time() - initial

# -----------------

print (deltaSort)
print (deltaOrderBubble)
print (deltaSort > deltaOrderBubble)