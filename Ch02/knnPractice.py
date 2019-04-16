#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 09:08:25 2019

@author: Emma
"""
import numpy as np
import operator



def createDataSet():
    dataSet=np.array([[1,2],[3,2],[5,6],[4,2],[6,9],[8,5]])
    labels=['A','B','A','A','B','A']
    return dataSet,labels

def classify(inX,dataSet,lables,k):
    size=dataSet.shape[0]
    diffMatrix=dataSet-np.tile(inX,(size,1))
    squaDiffMatrix=diffMatrix**2
    squaDistances=squaDiffMatrix.sum(axis=1)
    distances=squaDistances**0.5
    sortedIndencis=distances.argsort()
    classLabels={}
    for i in range(k):
        voteILabel=lables[sortedIndencis[i]]
        classLabels[voteILabel]=classLabels.get(voteILabel,0)+1
    sortedClassLabels=sorted(classLabels.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassLabels[0][0]
    

        
  
        
   


if __name__=="__main__":
   dataSet,labels=createDataSet()
   inX=[4,5]
   print(classify(inX,dataSet,labels,6))



    







