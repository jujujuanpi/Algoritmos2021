# Examen 02 - Funciones Pandas y Lambdas
import pandas as pd
from functools import reduce

def linedesign ():
    print ("#"*50)

# Pregunta 1 = Lista de pacientes atendidos por mes en el 2020

patientsMedellin = {}

patientsMedellin ["Enero"] = 32121
patientsMedellin ["Febrero"] = 14564
patientsMedellin ["Marzo"] = 65465
patientsMedellin ["Abril"] = 85202
patientsMedellin ["Mayo"] = 93213
patientsMedellin ["Junio"] = 100231
patientsMedellin ["Julio"] = 120213
patientsMedellin ["Agosto"] = 65421
patientsMedellin ["Septiembre"] = 46546
patientsMedellin ["Octubre"] = 46547
patientsMedellin ["Noviembre"] = 84651
patientsMedellin ["Diciembre"] = 140521

seriesPatientsMedellin = pd.Series (patientsMedellin)

linedesign()
print ("----- Pacientes tratados en Medellín durante el año 2020 -----")
print (seriesPatientsMedellin)
linedesign()

# Pregunta 2 = Información en cuatrimestres

print ("----- Pacientes tratados por cuatrimestre -----")

print ("PRIMER CUATRIMESTRE")
print (seriesPatientsMedellin ["Enero":"Marzo"])

print ("SEGUNDO CUATRIMESTE")
print (seriesPatientsMedellin ["Abril":"Junio"])

print ("TERCER CUATRIMESTRE")
print (seriesPatientsMedellin ["Julio":"Septiembre"])

print ("CUARTO CUATRIMESTRE")
print (seriesPatientsMedellin ["Octubre":"Diciembre"])
linedesign()

# Pregunta 3 = Promedio de pacientes atendidos por mes

print ("----- Promedio de pacientes atendidos por mes en el 2020 -----")
print (sum(seriesPatientsMedellin)/len (seriesPatientsMedellin))
linedesign ()

# Pregunta 4 = Lista de enfermedades en Bogotá en su primer semestre del 2020

dicDiseasesBogota = {
    "Enfermedad General" : [32121,14564,65465,85202,93213,100231],
    "COVID-19" : [0,0,223,3453,4543,43643],
    "Traumatismos" : [6545,43243,67657,435435,345345,43543],
    "Cáncer" : [6541,4334,4323,34545,5454,7675]
}

listMonths = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

dfDiseasesBogota = pd.DataFrame (dicDiseasesBogota, index = listMonths)

print ("----- Distribución de enfermedades de Bogotá en el primer semestre del 2020 -----")
print (dfDiseasesBogota)
linedesign()

# Pregunta 5 = Promedio Pacientes COVID-19 entre Abril y Junio

covidCases = {}
covidCases ["Enero"] = 0
covidCases ["Febrero"] = 0
covidCases ["Marzo"] = 223
covidCases ["Abril"] = 3453
covidCases ["Mayo"] = 4543
covidCases ["Junio"] = 43643

seriesCovidCases = pd.Series (covidCases)

print ("----- Promedio de pacientes con COVID-19 entre Abril y Junio -----")
print (sum(seriesCovidCases ["Abril":"Junio"])/len (seriesCovidCases ["Abril":"Junio"]))
linedesign()

# Pregunta 6 = Pacientes con traumatismos o cáncer en los primeros tres meses

print ("----- Pacientes con traumatismos o cáncer en los primeros tres meses -----")
print (dfDiseasesBogota [["Traumatismos", "Cáncer"]]["Enero":"Marzo"])
linedesign()

# Pregunta 7 = Lista FILTER de pacientes con Enfermedad General con más de 4000 casos

egCases = {32121,14564,65465,85202,93213,100231}

casesOver4K = lambda cases = 0 : cases >= 40000

listEGOver4K = list (filter(casesOver4K, egCases))

print ("----- Datos de Enfermedad General que superan 40,000 casos -----")
print (listEGOver4K)
linedesign()

# Pregunta 8 = Lista MAP del 10% de los pacientes con Cáncer

cancerCases = [6541,4334,4323,34545,5454,7675]

addTenPercent = lambda patients = 0 : patients * 0.1

listCancerCasesPlusTenPercent = list (map(addTenPercent,cancerCases))

print ("----- Casos de cáncer multiplicados por 10%")
print (listCancerCasesPlusTenPercent)
linedesign()

# Pregunta 9 = Lista REDUCE de la suma de los pacientes con traumatismos

traumaCases = [6545,43243,67657,435435,345345,43543]

addCases = lambda acumulado = 0, elemento = 0 : acumulado + elemento
totalTraumaCases = reduce (addCases,traumaCases)

print ("----- Total de casos de Traumatismo en el primer semestre -----")
print (totalTraumaCases)
linedesign()