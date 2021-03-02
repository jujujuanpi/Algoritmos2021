import pandas as pd

listaVariada = ['a',1,2,4.6]
print (listaVariada)

# Series son listas pero todas con la misma variable: todo numero o todo texto.
seriesPandas = pd.Series ([1,6,3])
print (seriesPandas)

dicGanancias = {}
dicGanancias ["Enero"] = 4300
dicGanancias ["Febrero"] = 4000
dicGanancias ["Marzo"] = 6050
dicGanancias ["Abril"] = 5600

seriesGanancias = pd.Series ([4300,4000,6050,5600])
print (seriesGanancias)

seriesGananciasDic = pd.Series (dicGanancias)
print (seriesGananciasDic)

# Dataframes son matrices, es decir un elemento mas grande, en pandas

nombres = [["Juan", "Karla"], ["Arturo", "Laura"]]

dataFrameNombres = pd.DataFrame (nombres)
print (dataFrameNombres)

matrizEstudiantes = {
                        "Grupo 1":['Karla', 'Mario', 'Laura'],
                        "Grupo 2":['Santi', 'Arturo', 'Vale'],
                        "Grupo 3":['Juan', 'Melany', 'Laura'],
                        "Grupo 4":['Mafer', 'Esteban', 'Iggy'],
}

dataFrameNombres = pd.DataFrame(matrizEstudiantes)
print (dataFrameNombres)

print ("#"*60)
print (dataFrameNombres ["Grupo 2"])

print ("#"*60)
print (dataFrameNombres.iloc [1:])

dicVentasMes = {
    "Marzo ($)" : [87645,83745,89745,68234],
    "Abril ($)" : [97364,42984,345978,345978],
    "Mayo ($)" : [479432,8724,789234,978234]
}

dataFrameVentas = pd.DataFrame (dicVentasMes, index = ["A", "B", "C", "D"])
print (dataFrameVentas)