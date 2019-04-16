#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:34:26 2019

@author: Emma
"""
import numpy as np
import re
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

def createVocabList(dataSet):
    vocabList=set([])
    for document in dataSet:
        vocabList|=set(document)
    return list(vocabList)

def setOfWords2Vec(vocabList,inputSet):
    retVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            retVec[vocabList.index(word)]+=1
        else:
            print("the word {} is not in my vocabulary!!!".format(word))
    return retVec

def trainNB0(trainMatrix,trainCategory):
    numberDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    cateCount={}
    TotalWordEachCate={}
    wordsVecEachCate={}
    for i in range(numberDocs):
        currentCategory=trainCategory[i]
        cateCount[currentCategory]=cateCount.get(currentCategory,0)+1
        TotalWordEachCate[currentCategory]=TotalWordEachCate.get(currentCategory,2)+sum(trainMatrix[i])
        wordsVecEachCate[currentCategory]=wordsVecEachCate.get(currentCategory,np.ones(numWords))+trainMatrix[i]
    for key in cateCount:
        cateCount[key]=float(cateCount[key])/numberDocs
        wordsVecEachCate[key]=np.log(wordsVecEachCate[key]/float(TotalWordEachCate[key]))
    return cateCount,wordsVecEachCate
        
        
def classifyNB(vec2Classify,cateCount,wordsVecEachCate):
    probCount=[]
    bestCate=None
    bestProb=None
    for key in cateCount:
        currentProb=np.log(cateCount[key])+sum(vec2Classify*wordsVecEachCate[key])
        if currentProb>bestProb or bestProb is None:
            bestCate=key
            bestProb=currentProb
        
    return bestCate
   
def textParse(bigString):
    import re
    listOfTokens=re.split('\\W*',bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]

def spamTest():
    docList=[];classList=[];
    for i in range(1,26):
        wordList=textParse(open('email/ham/{}.txt'.format(i)).read())
        docList.append(wordList)
        classList.append('ham')
        wordList=textParse(open('email/spam/{}.txt'.format(i)).read())
        docList.append(wordList)
        classList.append('spam')
    vocabList=createVocabList(docList)
    trainSet=range(50);testSet=[]
    for i in range(10):
        randIndex=int(np.random.uniform(0,len(trainSet)))
        testSet.append(trainSet[randIndex])
        del trainSet[randIndex]
    trainMat=[];trainClass=[]
    for i in trainSet:
        trainMat.append(setOfWords2Vec(vocabList,docList[i]))
        trainClass.append(classList[i])
    classProb,wordProbVec=trainNB0(trainMat,trainClass)
    errorCount=0
    for index in testSet:
        wordVector=setOfWords2Vec(vocabList,docList[index])
        if classifyNB(wordVector,classProb,wordProbVec)!=classList[index]:
            
            errorCount+=1
    return errorCount/float(len(testSet))
    
    

if __name__=='__main__':
   print(spamTest())
   
 