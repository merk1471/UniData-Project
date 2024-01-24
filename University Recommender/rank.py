#Developed by: Mark Samwaiel
#Date: June 6th 2023 
#Desc: A program to retrieve specific data from two csv files and manipulate it to rank universities in many ways using 12 unique functions.
#Inputs: The code does take input while it is running, it operates using arguments including but not limited to file names, country names, university codes, budgets, and degree names. 
#Output: This program does not output anything on its own. It will return information based on which function was called and which arguments were used. Error messages may appear in some cases such as the last function. 
SAMECOUNTRY = 500
SAMECONTINENT = 2000
DIFFERENTCONTINENTS = 5000
#Define the constants that are used in the 12th function. 
def readFiles(UniFileName, capitalsFileName):
    countries = []
    allUnivs = {}
    try:
        readC = open(capitalsFileName)
        lines = readC.readline()
        while lines != "":
            lines = readC.readline()
            lines = lines.rstrip()
            wordlist = lines.split(",")
            if len(wordlist) >=5:
                country = wordlist[0], wordlist[1], wordlist[5]
                countries.append(country)
#Inside of a try statement, search the capital file and seperate all words. If the line contains all indexes, create the countries list with the country, capital, and continent. 
        readU = open(UniFileName)
        linesu = readU.readline()
        while linesu != "":
            degrees = []
            linesu = readU.readline()
            linesu = linesu.rstrip()
            wordlist = linesu.split(",")
            if len(wordlist) >= 7:
                degrees.append(wordlist[5])
                oneUniversity = {}
                oneUniversity["intrank"] = int(wordlist[1])
                oneUniversity["name"] = wordlist[2]
                oneUniversity["country"] = wordlist[3]
                oneUniversity["natrank"] = int(wordlist[4])
                oneUniversity["degrees"] = (degrees)
                oneUniversity["cost"] = int(wordlist[6])
                oneUniversity["score"] = float(wordlist[7])
                for i in range (len(countries)):
                    for y in countries:
                            if y[0] == wordlist[3]:
                                cap = y[1]
                                cont = y[2]
                                oneUniversity["capital"] = cap                               
                                oneUniversity["continent"] = cont 
                                allUnivs[wordlist[0]]= (oneUniversity)  
#Inside of a try statement, search the universities file and seperate all words. If the line contains all indexes, add the degrees to the degree list and create the oneUniversity dictionary. Define all keys and elements.
#For all the countries, loop over every country. If the country being looped over matches the country in the university dictionary being created, add the corresponding capital and continent to the dictionary which is finally added to allUnivs dictionary. 
        readC.close()
        readU.close()               
    except IOError :
        return False 
    return allUnivs
#Close files, return False if a file cannot be found. Return the main dictionary containing all the info if no IOErrors occur. 

def findCountryByName(countryName, countries):
    try:
        for i in countries:
            if countryName == countries[i][0]:
             return countries[i]
    except IOError:
        return False
#In a try statement, search the countries list for the given country and if you find it return all the related info. If it is not found return False.  

def getAllCodes(allUnivs):
    code = []
    for i in allUnivs:
        code.append (i)
    codes = set(code)
    return codes
#Search the dictionary and add all codes to the code list. Create a set out of the list containing all university codes. 

def getDistinctCountries(allUnivs):
    countries = []
    for i in (allUnivs):
        countries.append((allUnivs[i]["country"]))
        distinctCountries = set(countries)
    return distinctCountries
#Search the dictionary and add all countries found to the country list. Create and return a set out of the list containing all countries with universites in the dictionary.

def getDistinctContinents(allUnivs):
    continents = []
    for i in (allUnivs):
        continents.append((allUnivs[i]["continent"]))
        distinctContinents = set(continents)
    return distinctContinents
#Search the dictionary and add all continents to the continent list. Create and return a set out of the list containing all continents with universites in the dictionary.

def getTopIntRank(countryName, allUnivs):
    countryName = countryName.upper()
    intRank = 100
    topUni = ()
    for i in allUnivs:
        if countryName == allUnivs[i]["country"].upper() and allUnivs[i]["intrank"] < intRank:
            intRank = allUnivs[i]["intrank"]
            topUni = allUnivs [i]["name"]
    return (intRank, topUni)
#Search the dictionary for international ranks in the given country name. Find the university with the lowest value for intRank and return its name and international rank. 

def getTopNatRank(countryName, allUnivs):
    countryName = countryName.upper()
    natRank = 100
    topUni = ()
    for i in allUnivs:
        if countryName == allUnivs[i]["country"].upper() and allUnivs[i]["natrank"] < natRank:
            natRank = allUnivs[i]["natrank"]
            topUni = allUnivs [i]["name"]
    return (natRank, topUni)
#Search the dictionary for national ranks in the given country name. Find the university with the lowest value for natRank and return its name and national rank. 

def getAvgScore(countryName, allUnivs):
    totalScore = 0 
    countryUnivs = 0
    countryName = countryName.upper()
    for i in allUnivs:
        if countryName == allUnivs[i]["country"].upper():
            totalScore += allUnivs[i]["score"]
            countryUnivs += 1
    if countryUnivs > 0:
        count = (totalScore / countryUnivs) 
 
    return round(count,2) 
#Search the dictionary for universities in the given country name. Add up scores and the number of universities, divide total score by the number of universities and return value rounded to 2 decimal places. 

def getRelativeScoreContinent(countryName, allUnivs):
    totalScore = 0 
    countryUnivs = 0
    highestScore = 0
    countryName = countryName.upper()
    for i in allUnivs:
        if countryName == allUnivs[i]["country"].upper():
            totalScore += allUnivs[i]["score"]
            countryUnivs += 1
        if countryName == allUnivs[i]["country"].upper():
            continent = allUnivs[i]["continent"].upper()
    if countryUnivs > 0:
        count = round((totalScore / countryUnivs),2)
    for i in allUnivs:
        if continent == allUnivs[i]["continent"].upper() and allUnivs[i]["score"] > highestScore:
            highestScore = allUnivs[i]["score"]
    avg = (count / highestScore) * 100
    return round(avg,2)
#Search the dictionary for universities in the given country name. Add up scores and the number of universities, divide total score by the number of universities, get value rounded to 2 decimal places. 
#Find the related continent, search it for the highest score, divide the country's average by the highest score, multiply the result by 100, return it rounded to 2 decimal places.

def getUnivWithCapital(countryName, allUnivs):
    univsWithCapital=set()
    countryName = countryName.upper()
    for i in allUnivs:
        if countryName == allUnivs[i]["country"].upper():
            capital = allUnivs[i]["capital"].upper()
    for i in allUnivs:
        if capital in (allUnivs[i]["name"].upper()):
            univsWithCapital.add(i)  
    return univsWithCapital

#Search the dictionary for the capital of the country given, search all universities in country for ones that contain the capital in their name. 
def studyInOnePlace(countryName, degrees, budget,allUnivs):
    countryName = countryName.upper()
    budget 
    allUnivs 
    codes=set()
    numberOfDegrees = 0
    degrees = set( [d.upper() for d in degrees])
    for i in degrees:
        numberOfDegrees += 1
    for i in allUnivs:
        if countryName == allUnivs[i]["country"].upper() and budget > ((allUnivs[i]["cost"]) * (numberOfDegrees)):
            for y in allUnivs[i]["degrees"]:         
                if all(x.upper() in y.upper() for x in degrees):
                    codes.add(i)                  
    return codes
#Find number of degrees entered to calculate cost. Search the dictionary for universities in the given country with a cost below the budget. If all degrees are contained in the university add its code to the set.  
def studyInTwoPlaces(firstCode, firstDegree,secondCode , secondDegree, budget,allUnivs):
    firstDegree = firstDegree.upper()
    secondDegree = secondDegree.upper()
    firstCode = firstCode.upper()
    secondCode = secondCode.upper()

    for i in allUnivs: 
        if i.upper() == firstCode:
            firstScore = allUnivs[i]["intrank"]
            firstCost = allUnivs[i]["cost"]
            for y in allUnivs[i]["degrees"]:
                if not firstDegree in y.upper():
                    raise ValueError("Something went wrong!")
        elif i == secondCode:
            secondScore = allUnivs[i]["intrank"]
            secondCost = allUnivs[i]["cost"]
            for y in allUnivs[i]["degrees"]:
                if not secondDegree in y.upper():
                    raise ValueError("Something went wrong!")
    if secondScore < firstScore:
        raise ValueError("Something went wrong!")
    for i in allUnivs:
        for y in allUnivs:
            if i.upper() == firstCode and y.upper() == secondCode:
                if allUnivs[i]["country"] == allUnivs[y]["country"]:
                    countryStatus = SAMECOUNTRY
                elif allUnivs[i]["continent"] == allUnivs[y]["continent"]:
                    countryStatus = SAMECONTINENT
                else:
                    countryStatus = DIFFERENTCONTINENTS
    totalCost = firstCost + secondCost + int(countryStatus)
    if totalCost < budget:
        return True
    else:
        return False
#Search the dictionary to find matching information for 2 codes given. Raise a ValueError if they do not have the desired degrees or if the second score is smaller than the first. 
#For all universities, check all the universities to find the intersection of the 2 universities. Compare the location of their countries and assign a value from the constants based on it.
#Calculate total cost and return True if it's below the budget, otherwise return False. 
#End of code. 