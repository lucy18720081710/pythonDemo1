import knn
group,labels = knn.createDataSet()
print(group)
print(labels)

# import knn
# knn.classify0([0.1,0.1], group, labels, 3)
print(knn.classify0([0.1,0.1], group, labels, 3))


reload(knn)
datingDataMat, datingLabels = knn.file2matrix("datingTestSet2.txt")
print(datingDataMat)
print(datingLabels[0:20])


import matplotlib
from numpy import *
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:, 2])
ax.scatter(datingDataMat[:,1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
print(plt.show())

reload(knn)
normMat, ranges, minVals = knn.autoNorm(datingDataMat)
print(normMat,   ranges, minVals)


print(knn.datingClassTest())


import os
print(os.getcwd())


print(knn.classifyPerson())


testVector = knn.img2vector("testDigits/0_13.txt")
print(testVector[0,0:30])
print(testVector[0,32:63])


print("knn.handwritingClassTest()")