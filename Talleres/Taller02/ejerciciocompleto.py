#---------- Crear un elemento donde muestre las ventas mes a mes de una empresa durante un año ---------- #
import pandas as pd

dicEarningsPerYear = {} # Se hace con series porque es solo un valor y una llave

dicEarningsPerYear ["January"] = 12345
dicEarningsPerYear ["February"] = 23456
dicEarningsPerYear ["March"] = 34567
dicEarningsPerYear ["April"] = 45678
dicEarningsPerYear ["May"] = 56789
dicEarningsPerYear ["June"] = 67890
dicEarningsPerYear ["July"] = 78901
dicEarningsPerYear ["August"] = 89012
dicEarningsPerYear ["September"] = 90123
dicEarningsPerYear ["October"] = 98765
dicEarningsPerYear ["November"] = 87654
dicEarningsPerYear ["December"] = 76543

seriesEarningsPerYear = pd.Series (dicEarningsPerYear)
print (seriesEarningsPerYear)

# Mostrar en pantalla las ganancias por trimestre

print ("1st Trimester")
print (seriesEarningsPerYear ["January":"March"])
print ("2nd Trimester")
print (seriesEarningsPerYear ["April":"June"])
print ("3rd Trimester")
print (seriesEarningsPerYear ["July":"September"])
print ("4th Trimester")
print (seriesEarningsPerYear ["October":"December"])

print ("Total 4th Trimester")
print (sum (seriesEarningsPerYear ["October":"December"]))


dicEarningsTrimesters = {}

dicEarningsTrimesters ["1st Trimester"] = sum (seriesEarningsPerYear ["January":"March"])
dicEarningsTrimesters ["2nd Trimester"] = sum (seriesEarningsPerYear ["April":"June"])
dicEarningsTrimesters ["3rd Trimester"] = sum (seriesEarningsPerYear ["July":"September"])
dicEarningsTrimesters ["4th Trimester"] = sum (seriesEarningsPerYear ["October":"December"])

seriesEarningsTrimesters = pd.Series (dicEarningsTrimesters) 
print (seriesEarningsTrimesters)

# Mostrar en pantalla las ganancias totales del año

print ("#"*50)
print ("Yearly earnings")
print (sum(seriesEarningsPerYear))

#---------- Ganancias por mes por departamento de Antioquia, Amazonas y Cundinamarca ---------- #

dicEarningsPerDepartment = { # Se usa un dataFrame porque son varias llaves con sus propios valores (matriz)
    "Antioquia" : [12345,23456,34567,45678,56789,67890],
    "Amazonas" : [98765,87654,76543,65432,54321,43210],
    "Cundinamarca" : [10293,19283,18273,17263,16253,56382]
}

listMonths = ["January", "February", "March", "April", "May", "June"]

dataFrameEarningsPerDepartment = pd.DataFrame (dicEarningsPerDepartment, index = listMonths)
print ("#"*50)
print (dataFrameEarningsPerDepartment)

# Mostrar en pantalla las ganancias por trimestres

print ("#"*50)
print ("1st Trimester")
print (dataFrameEarningsPerDepartment ["January":"March"])
print ("2nd Trimester")
print (dataFrameEarningsPerDepartment ["April":"June"])

# Mostrar en pantalla las ganancias de solo dos departamentos

print ("#"*50)
print ("Earnings for Antioquia and Amazonas")
print (dataFrameEarningsPerDepartment [["Antioquia", "Amazonas"]])

print ("#"*50)
print ("Earnings for Antioquia and Amazonas in 1st Trimester")
print (dataFrameEarningsPerDepartment [["Antioquia", "Amazonas"]]["January":"March"])