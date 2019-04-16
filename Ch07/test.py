#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:50:06 2019

@author: Emma
"""

from  adaboost import *

data,classLabel=loadSimpData()

print(data)
print(classLabel)

print(stumpClassify(data,0,1.5,'lt'))

