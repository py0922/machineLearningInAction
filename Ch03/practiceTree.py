#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:21:40 2019

@author: Emma
"""

from math import log
import operator
import matplotlib.pyplot as plt

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels
def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    classCount={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        classCount[currentLabel]=classCount.get(currentLabel,0)+1
    entrypy=0.0
    for key in classCount:
        prob=float(classCount[key])/numEntries
        entrypy+=-prob*log(prob,2)
    
    return entrypy 

def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedDataSet=featVec[:axis]
            reducedDataSet.extend(featVec[axis+1:])
            retDataSet.append(reducedDataSet)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntrypy=calcShannonEnt(dataSet)
    bestGainEnt=0.0
    bestFeature=-1
    for i in range(numFeatures):
        subEntrypy=0.0
        valueList=[item[i] for item in dataSet]
        uniqueValue=set(valueList)
        valueCount={}
        for value in uniqueValue:           
            subDataSet=splitDataSet(dataSet,i,value)
            prob=float(len(subDataSet))/len(dataSet)
            subEntrypy+=prob*calcShannonEnt(subDataSet)
        gainEntry=baseEntrypy-subEntrypy
        if gainEntry>bestGainEnt:
            bestGainEnt=gainEntry
            bestFeature=i
    return bestFeature
            
def majorityCnt(classList):
    classCount={}
    for value in classList:
        classCount[value]=classCount.get(value,0)+1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
    
            
def createTree(dataSet,labels):
    classList=[item[-1] for item in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeature=chooseBestFeatureToSplit(dataSet)
    bestFeatureLabel=labels[bestFeature]
    del labels[bestFeature]
    myTree={bestFeatureLabel:{}}
    valueList=[item[bestFeature] for item in dataSet]
    uniqueValue=set(valueList)
    for value in uniqueValue:
        subLabels=labels[:]
        myTree[bestFeatureLabel][value]=createTree(splitDataSet(dataSet,bestFeature,value),subLabels)
    return myTree

def classify(inputTree,featLabels,testVec):
    firstLabel=inputTree.keys()[0]
    secondDict=inputTree[firstLabel]
    featIndex=featLabels.index(firstLabel)
    for key in secondDict:
        if key==testVec[featIndex]:
            if type(secondDict[key]).__name__=='dict':
                return classify(secondDict[key],featLabels,testVec)
            else:
                return secondDict[key]

def storeTree(inputTree, fileName):
    import pickle
    fw=open(fileName,'w')
    pickle.dump(inputTree,fw)
    fw.close()
    
def grabTree(fileName):
    import pickle
    fr=open(fileName)
    return pickle.load(fr)
    
    
if __name__=="__main__":
    dataSet,labels=createDataSet()
#    chooseBestFeatureToSplit(dataSet)
    labels01=labels[:]
    myTree=createTree(dataSet,labels01)
    print(classify(myTree,labels,[1,0]))
    print("before store:")
    print(myTree) 
    storeTree(myTree,"classifierStorage.txt")
    newTree=grabTree("classifierStorage.txt")
    print("grab tree from the file")
    print(newTree)

    

    
    
    
 

   

    

    
  
   
    
  
    
    
    
    