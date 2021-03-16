import time

timeInitial = time.time()
print ("Hola a todos!")
time.sleep(2)
timeFinal = time.time()
delta = timeFinal - timeInitial
print (delta)

# Inicio conteo
tiempoInicial = time.time()
# Instrucciones
for i in range(1000):
    print (i)
# Cierre conteo
tiempoFinal = time.time()
deltaA = tiempoFinal - tiempoInicial
print(deltaA)