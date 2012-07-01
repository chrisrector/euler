# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:13:00 2012

@author: crector
"""
import math
import random
import sys

factor = 0


def hasDivisor(testNum):
    
    halfPoint = int(testNum/2)
    #print "  half point of ", testNum, "is ", halfPoint 
    if (halfPoint == 1):
        return 0
    
    i = 2
    while (i < halfPoint):
        tmpResult = float(testNum)/float(i)
        #print "    trying ", i, ", tmpResult=", tmpResult
        
        if ( tmpResult == math.ceil(tmpResult) ):
            return i
        
        i += 1
    
    return 0

def expMod(b, e, m):

    c=1
    i=1
    while (i <= e):
        c = (b*c) % m
        i+=1
        
    return c
        

def isPrime(testNum):
    
    n = testNum
    
    if ( testNum/2 == math.ceil(float(testNum)/2) ):
        return 0
    
    factored = 0
    currNum = n - 1
    s = 0
    d = 0
    while ( factored == 0):
        #print "factoring currNum", currNum
        dividend = float(currNum)/2
        if (dividend != math.ceil(dividend)):
            factored = 1
            d = currNum
        else:
            s += 1
        currNum = dividend
    
    #print "n=%d, s=%d, d=%d" % (n, s, d)
    
    if (s==1):
        print "no r values"
        return 0

    for k in range(0,1):
        a=random.randint(1, n)
        #a=3    
        print "testing k=%d, n=%d, s=%d, d=%d, a=%d" % (k, n, s, d, a)
        
        
        
        #x = long(math.pow(a, d)) % n
        #x = long(a**d) % n
        x = int(expMod(a, int(d), n))
    
    
        print "a=%d, x=%d" % (a, x)
        
        
        if ( x == 1 or x == n-1):
            print "x is 1 or n-1"  
        else:            
            r = 1
            nextk = 0
        
            while (r <= (s - 1) and nextk != 1):
                
                #x = math.pow(x, 2) % n
                x = (x**2) % n
                print "checking r=%d, x=%d" % (r, x)
                if (x==1):  return 0
                elif (x == n-1 ):
                    nextk = 1
                    break
                #if (x == n-1): 
                r += 1
                
            if ( nextk != 1): return 0

    return 1

#####################################################################

maxNum = math.ceil(math.log(sys.maxint, 2)) + 1 # Signedness
print "max num is ", maxNum

#test = 8462696833
#result = isPrime(test)
#print "prime test of ", test, " is ", result
#sys.exit(0)

targetNum = 600851475143 
#targetNum = 31
#targetNum = 13195
#result = hasDivisor(targetNum)

factor = targetNum #default, in case target is prime

halfPoint = int(targetNum/2)
j = 2
while ( j <= halfPoint):

    tmp = float(targetNum)/float(j)    
    
    #print "examining ", targetNum, " div by ", j
    tmp = float(targetNum)/float(j)
    
    if ( tmp == math.ceil(tmp) ):
       if ( isPrime(tmp) ):
           print "found prime factor ", tmp
           factor = tmp
           break
    j += 1

print "result is ", factor
    