#490Data
"""Program to do analysis on 490 data
"""

import csv

csv490 = 'C:\\Users\\fenichele\\github\\490Data.csv'

def readData():

    csvData = []
    with open(csv490,'r',encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            csvData.append(row)

    return csvData

def count490(bibVal):

    records = readData()

    bibcount = 0
    for row in records:
        if row[0] == bibVal and '490' in row[1]:
            bibcount += 1

    return bibcount

def distinctBibs():
    records = readData()
    bibList = []

    for row in records:
        if row[0] in bibList:
            pass
        else:
            bibList.append(row[0])

    return bibList

def findOnlyTwo():

    distBibs = distinctBibs()

    onlyTwoBibs = []
    for bib in distBibs:
        countBib = count490(bib)
        if countBib == 2:
            onlyTwoBibs.append(bib)

    return onlyTwoBibs

def shortenRecords():

    bibl = findOnlyTwo()

    records = readData()

    srecords = []

    for r in records:
        if r[0] in bibl:
            srecords.append(r)

    return srecords

def checkInd(filteredrows):

    inds = []
    acceptibleInds = [['1','0'],['0','1']]

    for o in filteredrows:
        ind = o[1][3:4]
        inds.append(ind)

    result = inds in acceptibleInds

    return result

def filterBib(bib):
    """returns a list of rows from the file with just the BIBs sent to it"""

    fbib = bib
    records = readData()

    frecords = list(filter((lambda x: x[0]==bib),records))

    return frecords

def filterBib490(frecords):
    """returns filtered list from the records of that bib from records, only those with a 490 are returned"""

    frecords = frecords

    ffrecords = list(filter((lambda x: x[1][0:3]=='490'),frecords))

    return ffrecords

def find490(testBib):
    """determines whether or not there are 2 490s in the list;
     one with first indicator 1 and one with first indicator 0"""

    #filter the records to just the bib
    filteredrows = filterBib(testBib)
    #filter the filtered list down to only those with 490s
    filteredrows = filterBib490(filteredrows)

    if len(filteredrows) != 2:
        return False
    else:
        result = checkInd(filteredrows)

    return result

def run490():
    """cycles through the distinct list of bibs and writes the results to the screen"""

    bibl = distinctBibs()

    goodBibs = []
    for bib in bibl:
        has490 = find490(bib)

        if has490:
            goodBibs.append(bib)

    return goodBibs




