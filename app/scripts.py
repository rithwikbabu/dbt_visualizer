import json

def readJson():
    with open('app/data/catalog.json') as json_file:
        data = json.load(json_file)
    return data

def getCatalog():
    data = readJson()
    for i in data['nodes']:
        data['nodes'][i].pop('unique_id')
        # for j in data['nodes'][i]:
        #     print(j)
    return data['nodes']

