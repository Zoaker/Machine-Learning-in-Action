from math import log
def calcShannonEnt (dataset) :
    numEntries = len(dataset)
    labelCounts = {}
    for featVec in dataset :
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return  shannonEnt
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels

def splitDataSet(dataSet, axis, value) :
    retDataSet = []
    for featVEC in dataSet :
        if featVEC[axis] == value:
            reducedFeatVec = featVEC[:axis]
            reducedFeatVec.extend(featVEC[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

myDat, labels=createDataSet()
value = splitDataSet(myDat, 0, 1)
print (value)
