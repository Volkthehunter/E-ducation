# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:05:51 2019

@author: Pongpanot
"""

import function as Inno
import key as key
#question = 'Why desert rat has longer nephridium than humans ?'
#ans_key = 'Because desert rat has less intake of water, so they must reabsorb the water back as much as possible.'
#ans = [['because', 'desert', 'rat', 'has', 'less', 'intake', 'of', 'water'], ['so', 'they', 'must', 'reabsorb','the', 'water', 'back', 'as', 'much', 'as', 'possible']]
keywordGuide = ['main', 'mainAdjective', 'verb', 'adverb', 'object', 'objectAdjective']
Qnum = int(input('Question Number : '))
key.showQuestion(Qnum)
ans=(input())
keyword = key.findKey(Qnum)
print(Inno.finalCheck(ans, keyword))