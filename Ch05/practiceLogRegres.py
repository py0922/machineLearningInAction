#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:11:15 2019

@author: Emma
"""
from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(fileName):
    dataMat=[];labelMat=[];
    fr=open(fileName)
    for line in fr.readlines():
        currentLine=array(line.strip().split())
        lineArr=[1.0]
        for i in range(len(currentLine)-1):
            lineArr.append(float(currentLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(currentLine[-1]))
    return dataMat,labelMat
def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradDescent(dataMat,labelMat):
    dataMatrix=mat(dataMat)
    labelMatrix=mat(labelMat).transpose()
    m,n=dataMatrix.shape
    alpha=0.001
    maxCycles=1000
    weights=ones((n,1))
    for i in range(maxCycles):
        h=sigmoid(dataMatrix*weights)
        error=labelMatrix-h
        weights=weights+alpha*dataMatrix.transpose()*error
    return weights

def stocGradDescent(dataMat,labelMat,numCycles,alpha):
    m,n=shape(dataMat)
    weights=ones(n)
    for i in range(numCycles):
        dataIndex=range(m)
        for j in range(m):
            alpha01=4.0/(1+i+j)+alpha
            randIndex=int(random.uniform(0,len(dataIndex)))
            h=sigmoid(sum(dataMat[dataIndex[randIndex]]*weights))
            error=labelMat[dataIndex[randIndex]]-h
            weights=weights+alpha01*error*dataMat[dataIndex[randIndex]]
            del dataIndex[randIndex]
    return weights
    

def classifyVector(inX,weights):
    prob=sigmoid(sum(inX*weights))
    if prob>0.5:
        return 1.0
    else:
        return 0.0
    


def plotBestFit(weights,fileName):
    dataMat,labelMat=loadDataSet(fileName)
    dataArr = array(dataMat)
    n = shape(dataArr)[0] 
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()

def test(weights,testMat,testLalel):
    errorCount=0
    for i in range(len(testMat)):
        if int(classifyVector(array(testMat[i]),weights))!=int(testLalel[i]):
            errorCount+=1
    errorRate=errorCount/float(len(testLabel))
    print("the error rate of this test is {}".format(errorRate))
    return errorRate


def multiTest(n,numCycles,alpha):
    errorRate=0.0
    for i in range(n):
        dataMat,labelMat=loadDataSet('horseColicTraining.txt')
        weights=stocGradDescent(array(dataMat),labelMat,numCycles,alpha)
        testMat,testLabel=loadDataSet('horseColicTest.txt')
        errorRate+=test(weights,testMat,testLabel)
    avarageErrrorRate=errorRate/n
    print("the avarege error rate is: {}".format(avarageErrrorRate))
    return avarageErrrorRate
                   
        
if __name__=='__main__':
#    x=arange(50,500,50)
#    y=[]
#    for i in x:
#        y.append(multiTest(10,i,0.006))
#    fig = plt.figure()
#    ax = fig.add_subplot(111)
#    print(x)
#    print(y)
#    ax.plot(x, y)
#    plt.xlabel('X1'); plt.ylabel('X2');
#    plt.show()
#    
    multiTest(10,100,0.01)
#    dataMat,labelMat=loadDataSet('horseColicTraining.txt')
#    weights=stocGradDescent(array(dataMat),labelMat,200,0.01)
#    print(weights)
#    
    
    

    
    
    
    
    