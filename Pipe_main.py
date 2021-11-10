import json
from requests import api
from api_functions import getApiInfo
from cleaning_functions import read_dataset
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Aquí combinamos los resultados de la Base de datos con la información de la API ya filtrada.
def combine_result(apiData, dataset):
    result = {
        "pollution":[],
        "deaths":[],
        "country":[]
    }
    for key in dataset.keys():
        if(key in apiData.keys()):
            result["pollution"].append(dataset[key])
            result["deaths"].append(apiData[key])
            result["country"].append(key)
    return result

  
def generateData():
    apiData = getApiInfo()
    dataset = read_dataset()
    result = combine_result(apiData, dataset)
    f = open("./Data/result.csv", "w")
    f.write("country,deaths,pollution\n")
    for i in range(len(result["country"])):
        line = f'{result["country"][i]},{result["deaths"][i]},{result["pollution"][i]}\n'
        f.write(line)
        
