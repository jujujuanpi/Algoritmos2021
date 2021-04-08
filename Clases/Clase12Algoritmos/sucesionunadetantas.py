# Ejemplo Algoritmo, creación de algoritmo para leer una sucesión
# SUCESIÓN: 3, 5, 7, 11, 19
#                             Calcular el número n-ésimo de la sucesión (cuál sigue)

# Número 1 = 3 (2**0)+3
# Número 2 = 5 (2**1)+3
# Número 3 = 7 (2**2)+3
# Número 4 = 11 (2**3)+3
# Número 5 = 19 (2**4)+3

def sucesionEjemplo (n):
    return (2**(n-1)) + 3

print (sucesionEjemplo(1))