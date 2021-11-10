import requests

#Nos traemos la API
api = "https://ghoapi.azureedge.net/api/"
indicator_endpoint = api + "/indicator/"
dimensions_endpoint  = api + "/DIMENSION"

#Filtramos la API para obtener los valores que necesitamos.
def get_country_values():
    data = requests.get(dimensions_endpoint + "/COUNTRY/DimensionValues")
    raw_data = data.json()
    result = {}
    for element in raw_data["value"]:
        result[element["Code"]] = element["Title"].lower().replace(" ", "_")

    return result

#Nos tramos las muertes causadas por contaminación de cada pais.
def get_air_pollution_deaths(countryLabels):
    data = requests.get("https://ghoapi.azureedge.net/api/AIR_11")
    raw_data = data.json()
    result = {} 
    for element in raw_data["value"]:
        country = element["SpatialDim"]
        value = element["NumericValue"]
        country_label = countryLabels[country]
        if(country_label not in result.keys() and value > 0.0):
            result[country_label] = 0
        if(value > 0.0):
            result[country_label] += value
    return result



def getApiInfo():
    countryLabels = get_country_values()
    result = get_air_pollution_deaths(countryLabels)
    return result
