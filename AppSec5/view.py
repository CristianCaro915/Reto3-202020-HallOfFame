"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.1
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from App import controller
import datetime
from DISClib.ADT import map as m
import numpy as np
from DISClib.ADT import orderedmap as om
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
accidents_file = 'us_accidents_small.csv'
# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Requerimento 1")
    print("4- Requerimento 2")
    print("5- Requerimento 3")
    print("6- Requerimento 4")
    print("7- Requerimento 5")
    print("8- Requerimento 6")
    print("0- Salir")
    print("*******************************************")

def printRespuesta():
    print("---------------------------------------------------")
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        printRespuesta()
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de accidentes ....")
        controller.loadData(cont, accidents_file)
        print('Accidentes cargados: ' + str(controller.accidentesSize(cont)))
        printRespuesta()

    elif int(inputs[0]) == 3:
        printRespuesta()
        print("\nBuscando los accidentes en una fecha por severidad... ")
        StartDate = input("Fecha (YYYY-MM-DD): ")
        
        print("\n {0:<10}{1:>10}           {2:>10}".format("Severidad", "Fecha" ,"Cantidad de accidentes")) 
        print("-------------------------------------------------------------")
        for severity in range (1,5):
           severity=str(severity)
           numaccidentes = controller.getaccidentesByRangeCode(cont, StartDate, severity) 
           if numaccidentes>0:
            print("   {0:<10}{1:>10}           {2:>10}".format(severity, StartDate ,numaccidentes)) 
        printRespuesta()
            
    elif int(inputs[0]) == 4:
        printRespuesta()
        initialDate = controller.getInitialDate(cont)
        finalDate = input("Rango Final: (YYYY-MM-DD): ")
        total = controller.getAccidentsByRange(cont, initialDate, finalDate)
        print("\nTotal de accidentes en el rango de fechas: " + str(total[0]))
        print("Fecha con mas accidentes: {}, numero de accidentes {}".format(total[1]['value'],total[1]['key']))
        printRespuesta()

    elif int(inputs[0]) == 5:
        printRespuesta()
        initialDate = input("Fecha Inicial: (YYYY-MM-DD): ")
        finalDate = input("Fecha Final: (YYYY-MM-DD): ")
        total = controller.getAccidentsByRange(cont,initialDate ,finalDate)
        print("\nTotal de accidentes en el rango de fechas: {} ".format(total[0]) )
        print("La severidad mas frecuente es {} con {} accidentes en el rango de fechas.".format(total[2]['key'],total[2]['value']))
        printRespuesta()

    elif int(inputs[0]) == 6:
        printRespuesta()
        initialDate = input("Fecha Inicial: (YYYY-MM-DD): ")
        finalDate = input("Fecha Final: (YYYY-MM-DD): ")
        total = controller.getAccidentsByRangeState(cont,initialDate ,finalDate)
        print("El estado que mas accidentes dentro del rango de fechas es: {} con {} accidentes".format(total[0],total[1]))
        total = controller.getAccidentsByRange(cont, initialDate, finalDate)
        print("Fecha con mas accidentes: {}, numero de accidentes {}".format(total[1]['value'],total[1]['key']))
        printRespuesta()
    
    elif int(inputs[0]) == 7:
        printRespuesta()
        initialHour = input("Hora Inicial: (HH:SS): ").split(":")
        finalHour = input("Hora Final: (HH:SS): ").split(":")
        total = controller.getAccidentsByRangeHour(cont,initialHour ,finalHour)
        print("\nTotal de accidentes en el rango de horas: {} ".format(total[0]) )
        accidenteshora=total[0]
        resu=total[2]
        acctot=controller.getsizeaccidentes(cont)
        for i in range (2,6):
            if om.contains(resu,i):
                num=om.get(resu,i)
                print ("Severidad: {} numero de accidentes: {}, porcentaje de severidad relativo a la hora: {:2.0f}%".format(i-1,num['value'], 100*num['value']/total[0]))
            else:
                print ("Severidad: {} numero de accidentes: {}, porcentaje de severidad: {}%".format(i,0,0))
        print("Porcentaje de severidad del rango de hora respecto a accidentes total {:2.0f}%".format(100*int(accidenteshora)/int(acctot)))
        printRespuesta()
    
    elif int(inputs[0]) == 8:
        printRespuesta()
        lat = np.radians(float(input("Latitud: ")))
        lng = np.radians(float(input("Longitud: ")))
        radio = float(input("Radio (en millas): "))
        res=controller.getaccidentesByDistance(cont,lng,lat,radio)
        dicdias={"0":"Lunes","1":"Martes","2":"Miercoles","3":"Jueves","4":"Viernes","5":"Sabado","6":"Domingo"}
        tot=0
        for i in range (0,7):
            if om.contains(res,i):
                tot+=om.get(res,i)['value']
                print("Día: {} numero de accidentes {}".format(dicdias[str(i)],om.get(res,i)['value']))
            else:
                print("Día: {} numero de accidentes {}".format(dicdias[str(i)],0))
        print("Total de accidentes: {}".format(tot))
        printRespuesta()
    else:
        sys.exit(0)
sys.exit(0)
