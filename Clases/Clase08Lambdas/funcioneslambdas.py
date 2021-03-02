def linedesign ():
    print ("#"*50)

linedesign()
print ("Hola a todos.")
linedesign()

def linedesigns (cantidad = 30):
    print ("#"*cantidad)

linedesigns ()
print ("Hola a nadie.")
linedesigns(10)

def sumar (a,b):
    suma = a+b
    return suma

linedesign()
print (sumar (2,6))
linedesign()

def restar (a,b):
    resta = a-b
    return resta

linedesign()
print (restar (6,2))
linedesign()

def multiplicar (a,b):
    multiplo = a*b
    return multiplo

linedesign()
print (multiplicar (2,6))
linedesign()

def dividir (a,b):
    division = a/b
    return division

linedesign()
print (dividir (6,2))
linedesign()

def calculadora (funcion, a,b):
    return funcion (a,b)

print (calculadora(sumar, 12,14))

linedesignLambda = lambda cantidad=50 : print ("#"*cantidad) # Lambda indica que es anónimo, a la izquierda donde esta x se ponen los parámetros, y a la derecha las acciones.

linedesignLambda()

sumarL = lambda a=0 , b=0 : a+b
print (sumarL(2,6))

restarL = lambda a=0 , b=0 : a-b
print (restarL(6,2))

multiplicarL = lambda a=0 , b=0 : a*b
print (multiplicarL(2,6))

dividirL = lambda a=0 , b=0 : a/b
print (dividirL(6,2))

calculadoraL = lambda func = sumarL, a=0, b=0 : func (a,b)
linedesignLambda()
print (calculadoraL (multiplicarL, 2,2))

listaEdades = [12,53,34,64,17,22]
listaEdades2 = [55,15,68,73,16,24]

maximosL = lambda x = [], y = [] : print (max(x), max(y))

linedesignLambda()
maximosL (listaEdades, listaEdades2)

mayorEdad = lambda edad = 0 : edad>=18
print(mayorEdad(14))
print(mayorEdad(19))

mayores = list (filter(mayorEdad, listaEdades))
print (mayores)