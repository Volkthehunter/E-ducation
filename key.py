# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:04:26 2019

@author: Pongpanot
"""

def findKey(index):
  g = open('Keys.txt','r')
  Keylist = g.readlines()
  return Keylist[int(index)-1]
  g.close()

def showQuestion(index):
  f = open('Questions.txt','r')
  Qlist=f.readlines()
  print(Qlist[int(index-1)])
  f.close()