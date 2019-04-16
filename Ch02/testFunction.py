#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 06:23:22 2019

@author: Emma
"""

import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import * 

reload(kNN)

group,labels=kNN.createDataSet()


print(kNN.classify0([0,0],group,labels,3))



#datingDataMat,datingDataLabels=file2matrix('datingTestSet2.txt')

#print(datingDataMatrix)
#print(datingDataLabels)

#fig=plt.figure()
#ax=fig.add_subplot(111)
#print(datingDataMat[:1])
#print(datingDataMat[:2].size)
#ax.scatter(datingDataMat[:,0],datingDataMat[:,1],20*array(datingDataLabels),array(datingDataLabels))
#plt.show()

#normalMat,ranges,minVals=kNN.autoNorm(datingDataMat)

#datingClassTest()

#(normalMat)
#print(ranges)
#print(minVals)

#print(array([10,1000,0.5]))
#classifypPerson()


#kNN.handwritingClassTest()

def classifypPerson():
    resultList=['not at all','in samll doses','in large doses']
    percentTags=float(raw_input("percentage of time spent playing video games?"))
    ffMiles=float(raw_input("frequent flier miles earned per year?"))
    iceCream=float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels=kNN.file2matrix('datingTestSet2.txt')
    normalMat,ranges,minVals=kNN.autoNorm(datingDataMat)
    inArr=array([ffMiles,percentTags,iceCream])
    classifierResult=kNN.classify0((inArr-minVals)/ranges,normalMat,datingLabels,3)
    print("You will probably like this person: ",resultList[classifierResult-1])
    


#classifypPerson() 