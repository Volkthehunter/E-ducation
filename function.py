# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:05:52 2019

@author: Pongpanot
"""


from main import Qnum
import key as key
keywordGuide = ['main', 'mainAdjective', 'verb', 'adverb', 'object', 'objectAdjective']
keyword = key.findKey(Qnum)

def sentenceunite(ans):
  ans = ans.replace(', ','#').strip('.').split('#')
  i = 0
  for elem in ans:
    elem = elem.lower().split()
    ans[i] = elem
    i += 1
  return (ans)
def checkKey(function, keyword, index, ans):
  check = 0
  if(keyword[index][function] == 0):
    check = -1
  pt = -1
  for elem in ans[index]:
    pt += 1
    if(elem == keyword[index][function]):
      check = 1
      break
    if (check == 1):
     break
  if (check == 1):
    return pt
  elif(check == -1):
    return 'No need to check'
  else:
    return 'Not Found'
def finalCheck(ans, keyword):
  count = 0
  for i in range(len(keyword)):
    for elem in keywordGuide:
      if(checkKey(elem, keyword, i, sentenceunite(ans)) == 'Not Found'):
        count = 1
        break
  if(count == 0):
    return True
  else:
    return False
