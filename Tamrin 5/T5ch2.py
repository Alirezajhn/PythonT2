
cityList = ["city1","city2","city3","city4","city5","city6"]
populationList = [300000, 1000000, 3800000, 500000, 1900000, 100000]
areaListSquarekilometer = [100, 200, 500, 150, 300, 100]

def changeHecKilometer(areaListSquarekilometer):
    areaListHec=[area*100 for area in areaListSquarekilometer]
    return areaListHec

def densitycalc(populationList):
    densityList=[]
    for i in range(6):
        density=populationList[i]/changeHecKilometer(areaListSquarekilometer)[i]
        densityList.append(density)
        
    return densityList


def showCityDensity(cityList):
    dictDensity={city:density for city,density in zip(cityList,densitycalc(populationList))}
    print("List of cities by population density")
    print("----------------------------")
    print("City\tDensity")
    for city,density in dictDensity.items():
        print(city,"\t",density)
    print("*******************************")
    print("List of high-Density cities")
    print("----------------------------")
    print("City\tDensity")
    dictHighDensity={city:density for city,density in zip(cityList,densitycalc(populationList))if density>=50}
    for city,density in dictHighDensity.items():
        print(city,"\t",density)
        
#----------------------------main-----------------------------------------------
showCityDensity(cityList)