jsonStrA = '[{"name":"pivo","price":7.99},{"name":"vino","price":35.99},{"name":"rakija","price":50}]'
jsonStrB = '[{"name":"paprika","price":11.99},{"name":"jaja","price":11.99},{"name":"kobasice","price":18.04}]'
jsonStrC = '[{"name":"sir","price":35.14},{"name":"slanina","price":40.54},{"name":"rajčica","price":9.99}]'


import json

def sortJsonArray():
    jsonArr = json.loads(jsonStrB)
    jsonArr = sorted(jsonArr, key = lambda x: x["name"], reverse=True) #sort by name desc
    jsonArr = sorted(jsonArr, key = lambda x: x["price"]) #sort by price asc
    return jsonArr


if __name__ == "__main__":
    print(sortJsonArray())
