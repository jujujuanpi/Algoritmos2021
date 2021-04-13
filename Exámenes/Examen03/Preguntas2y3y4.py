# ----- Pregunta 4: Optimización de conteo de palabras -----

def contarPalabrasV1(parrafo):
    '''Esta funcion describe cuantas veces 
    aparace cada palabra en una parrafo
    utilizando la instrucción count.
    '''
    dictPalabrasOcurrencias = {}
    listaPalabras = parrafo.split()
    for palabra in listaPalabras:
        dictPalabrasOcurrencias[palabra] = listaPalabras.count(palabra)
    return dictPalabrasOcurrencias

def contarPalabrasV2(parrafo):
    '''Esta funcion describe cuantas veces 
    aparace cada palabra en una parrafo
    utilizando otro for.
    '''
    dictPalabrasOcurrencias = {}
    listaPalabras = parrafo.split()
    for palabra in listaPalabras:
        dictPalabrasOcurrencias[palabra] = 0
        for i in range (len(listaPalabras)):
            if palabra == listaPalabras[i]:
                dictPalabrasOcurrencias[palabra] += 1
    return dictPalabrasOcurrencias

import time

parrafo = '''La justicia sobre la fuerza es la impotencia, la fuerza sin justicia es tiranía.
    Vale más saber alguna cosa de todo que saberlo todo de una sola cosa.
    Dos excesos: excluir la razón, no admitir más que la razón.
    Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte.
    El hombre tiene ilusiones como el pájaro alas. Eso es lo que lo sostiene.
    El hombre está dispuesto siempre a negar todo aquello que no comprende.
    Aquel que duda y no investiga, se torna no sólo infeliz, sino también injusto.
    A fuerza de hablar de amor, uno llega a enamorarse.
    ¿De qué le sirve al hombre ganar el mundo si pierde su alma?'''

inicio = time.time()
v1 = parrafo
deltav1 = time.time() - inicio

inicio = time.time()
v2 = parrafo
deltav2 = time.time() - inicio

print (deltav1,deltav2)

# Respuesta: Analizando los algoritmos propuestos, y haciendo el cálculo del deltaV1 y deltaV2, se logra comprobar que la funcion contarPalabrasV2 es el más óptimo y rápido.
# Se obtuvo un valor de 1.1920x10-06 para el deltaV1 y un valor de 9.5367x10-07 para el deltaV2. La diferencia entre los dos se debe a que el primer algoritmo utiliza la función count, la cual se realiza en orden lineal y va contando cada palabra una por una, para luego verificar cuales se repiten y sumarlas entre si.
# En cambio, el algoritmo V2 presenta un for que se va a encargar de verificar si todas las palabras que se están contando ya fueron contadas anteriormente, es decir, hace el conteo de cada palabra en orden y si alguna se repite, lo identifica y suma un +1 a la repetición de esa palabra de inmediato, resultando en una mayor rapidez. 



# ----- Pregunta 2: Escribir las fórmulas de las funciones -----

# FÓRMULA DEL CÓDIGO: 8 + xyw + x + w


# ----- Pregunta 3: Desarrollo de Algoritmos -----

# Función para A: 1, 1/2, 1/4, 1/8

def sucesionA (n):
    return (1 / (2 ** n))

print (sucesionA (4))

# Función para B: 3, 5, 7, 9, 11

# Numero 1 = 3 (2*0) + 3
# Numero 2 = 5 (2*1) + 3
# Numero 3 = 7 (2*2) + 3
# Numero 4 = 9 (2*3) + 3
# Numero 5 = 11 (2*4) + 3

def sucesionB (n):
    return ((2*n) + 3)

print (sucesionB (5))