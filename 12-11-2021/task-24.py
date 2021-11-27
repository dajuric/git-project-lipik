def getChange(amount, price):
    toReturn = amount - price
    
    fiveKunas = toReturn // 5
    toReturn = toReturn % 5

    twoKunas = toReturn // 2
    toReturn = toReturn % 2

    oneKuna = toReturn // 1
    toReturn =  toReturn % 1

    toReturn = int(toReturn * 100 * 100)
    fifyLipas = toReturn // 50
    toReturn =  toReturn % 50

    #TODO: 10 lipas
    #TODO: 5 lipas
    #TODO: 2 lipas

    twentyLipas = toReturn // 20
    toReturn = toReturn % 20

    return {"fiveKn": fiveKunas, "twoKn": twoKunas, "oneKn": oneKuna, 
            "fifyLps": fifyLipas, "twentyLps": twentyLipas, "oneLps": toReturn }

print(getChange(20, 3.99))