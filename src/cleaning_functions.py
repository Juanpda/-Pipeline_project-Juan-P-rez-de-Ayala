import csv

#Con esta función traemos el csv y lo filtramos 

def read_dataset():
    f = open("./Data/co2_emissions_tonnes_per_person.csv", 'r')
    raw_data = list(csv.reader(f, delimiter=',', quotechar='"'))
    result = {}
    for line in raw_data[1:]:
        country = line[0].lower().replace(" ", "_")
        result[country] = line[-3]
    f.close()
    return result
