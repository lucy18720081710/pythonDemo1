import trees
reload(trees)
myDat,labels=trees.createDataSet()
print(myDat)
print(trees.calcShannonEnt(myDat))

myDat[0][-1]="maybe"
print(myDat)
print(trees.calcShannonEnt(myDat))

a=[1,2,3]
b=[4,5,6]
a.append(b)
print (a)
a.extend(b)
print(a)

print(reload(trees))
myDat,labels = trees.createDataSet()
print (myDat)
print(trees.splitDataSet(myDat,0,1))
print(trees.splitDataSet(myDat,0,0))

print(reload(trees))
myDat,labels=trees.createDataSet()
print(trees.chooseBestFeatureToSplit(myDat))
print(myDat)

reload(trees)
myDat,labels = trees.createDataSet()
myTree = trees.createTree(myDat,labels)
print (myTree)

import treePlotter
print (treePlotter.createPlot())
