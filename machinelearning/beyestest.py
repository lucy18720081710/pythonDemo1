import bayes
listOposts,listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOposts)
print (myVocabList)

print (bayes.setOfWords2Vec(myVocabList,listOposts[0]))
print (bayes.setOfWords2Vec(myVocabList,listOposts[3]))

from numpy import *
print(reload(bayes))
listOposts,listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOposts)
trainMat = []
for postinDoc in listOposts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb = bayes.trainNBO(trainMat,listClasses)
print(pAb)
print (p0V)
print(p1V)

reload(bayes)
print(bayes.testingNB() )

