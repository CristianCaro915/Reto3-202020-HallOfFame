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
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

 """
    	Este código fue tomado de la entrega del grupo 1 de la secci;on 4 de EDA 2020-20.
 """

import config as cf
from App import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    analyzer = model.newAnalyzer()
    return analyzer

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, accidentsfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    accidentsfile = cf.data_dir + accidentsfile
    input_file = csv.DictReader(open(accidentsfile, encoding="utf-8"),
                                delimiter=",")
    for accident in input_file:
        model.addAccident(analyzer, accident)
    return analyzer


# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def accidentsSize(analyzer):
    
    return model.accidentsSize(analyzer)


def indexHeight(analyzer):
    
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    
    return model.indexSize(analyzer)


def minKey(analyzer):
    
    return model.minKey(analyzer)


def maxKey(analyzer):
    
    return model.maxKey(analyzer)

def getAccidentsBeforeDate(analyzer, date):
    #-------------------
    try:
        separar=date.split("-")
        anio= int(separar[0])
        mes= int(separar[1])
        dia= int(separar[2])
        if dia>1 and mes>1:
            dia=dia-1
        if dia==1 and mes>1:
            mes=mes-1
            dia=31
        if dia==1 and mes==1:
            anio=anio-1
            mes=12
            dia=31
        fecha = str(anio)+"-"+str(mes)+"-"+str(dia)

        newDate1 = datetime.datetime.strptime(fecha, '%Y-%m-%d')
        return model.getAccidentsBeforeDate(newDate1.date(),analyzer)
    except:
        return None 

def getAccidentsByDate(analyzer, date):
    try:
        newDate = datetime.datetime.strptime(date, '%Y-%m-%d')
        return model.getAccidentsByDate(newDate.date(),analyzer)
    except:
        return None 

def getAccidentsByDateRange(analyzer, date1, date2):
    try:
        newDate1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        newDate2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        return model.getAccidentsByDateRange(newDate1.date(),newDate2.date(),analyzer)
    except:
        return None 

def getStateByDateRange(analyzer, initialDate, finalDate):
    try:
        newDate1 = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
        newDate2 = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
        return model.getStateByDateRange(newDate1.date(),newDate2.date(),analyzer)
    except:
        return None

      
def accidentsByTimeRange(time1, time2, analyzer):
    try:
        oftime1 = model.timefix(time1)
        oftime2 = model.timefix(time2)
        return model.accidentsByTimeRange(oftime1,oftime2,analyzer)
    except:
        return None

def getLatitudRange(lat,lon,radius,analyzer):
    try:
        return model.getLatitudeRange(lat,lon,radius,analyzer)
    except:
        return None