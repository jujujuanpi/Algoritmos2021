lista = [2,25,34,65,8]

potenciador = lambda valor=0 : valor **2
print (potenciador(4))
listaCuadrados = list (map(potenciador, lista))
print (listaCuadrados)

listaCuadradosPrueba = []
for elemento in lista :
    valor = elemento **2
    listaCuadradosPrueba.append (valor)

print ("#"*50)
print (listaCuadradosPrueba)

# Elevar al cuadrado todos los valores de una lista

retornarListaCuadrados = lambda listaEntrada = [] : list(map(potenciador, listaEntrada))
lista4 = [4,5,24,63,20]
ListaCuadrados4 = retornarListaCuadrados(lista4)
print ("#"*50)
print (ListaCuadrados4)

# Función lambda para restar dos números

restarN = lambda valor=0, n=0 : valor - n
print ("#"*50)
print (restarN(3,1))

# Restar todos los valores de una lista por un número ---> SE USA SI ES UN ÚNICO NUMERO N QUE RESTA A LO DEMÁS

n = int (input("Ingrese el valor a restar:"))
restarN2 = lambda valor : valor - n
restarNLista = list(map(restarN2, lista4))
print ("#"*50)
print (restarNLista)

# Normalizar con Lambda = Dividir por el número mayor

lista5 = [23,53,745,27,2,85]
mayor = max (lista5)
dividir = lambda valor = 0 : round (valor/mayor,2) # Round para redondear
listaNormalizada = list (map(dividir,lista5))
print ("#"*50)
print (listaNormalizada)

# EJEMPLO #1: IMC
pesos = [56,57,85,46,89]
estaturas = [1.56,1.57,1.85,1.46,1.89]

imc = lambda peso = 0 , estatura = 1 : round (peso/estatura **2,2)
listaImc = list (map(imc,pesos,estaturas))
print ("#"*50)
print (listaImc)

# EJEMPLO #2: Área de un Triángulo
bases = [2,34,2,5,345,9]
alturas = [23,345,6,67,23]
divisores = [2,2,2,2,2]

calcularAreaTriangulo = lambda base = 0, altura = 0, divisor = 1 : round ((base*altura)/divisor,4)
listaAreasTriangulo = list (map(calcularAreaTriangulo,bases,alturas,divisores))
print ("#"*50)
print (listaAreasTriangulo)

# Funciones Reduce
from functools import reduce

lista6 = [1,2,3,4,5]

sumarElementos = lambda acumulado = 0, elemento = 0 : acumulado + elemento
sumar = reduce (sumarElementos,lista6)
print (sumar)

multiplicarElementos = lambda acumulado = 0, elemento = 1 : acumulado * elemento
multiplicar = reduce (multiplicarElementos,lista6)
print (multiplicar)