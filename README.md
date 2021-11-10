# Pipeline_project-JuanPerezdeAyala

En este proyecto vamos a trabajar para combinar la información de un Dataset con la información de una API y realizar un estudio sobre la contaminación en los paises comparándola con su mortalidad. El objetivo es lograr un documento en python que realice todo el filtrado mediante una sola ejecución.

El documento se compone principalmente de:
- Carpeta src que contiene dentro el código (main, cleaning y api).
- Jupyter notebook para la visualización.
- Readme.md explicativo.

La principales librerías que he utilizado son:
import json, 
from requests import api, 
from api_functions import getApiInfo, 
from cleaning_functions import read_dataset, 
import seaborn as sns, 
import matplotlib.pyplot as plt, 
import numpy as np, 
import pandas as pd.
