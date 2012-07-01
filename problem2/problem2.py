# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:13:00 2012

@author: crector
"""


prevNum = 1
currNum = 2;
total = 0;

while currNum < 4000000:

    if (currNum % 2 == 0):
        total += currNum
    
    newNum = prevNum + currNum
    prevNum = currNum
    currNum = newNum

        
print "answer is ", total