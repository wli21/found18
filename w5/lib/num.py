"""
Rewrite from num.luo

@author: Weijia Li
"""

from __future__ import division
from lib.testEngine import O
from lib.sample import Sample
import random, math

class Num:

    def same(x): return x
    
    def __init__(self,inits=[],f=same):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = 10**32
        self.hi = -10**32
        self.some = Sample()
        self.w = 1
        [self.numInc(x) for x in inits]

    def numInc(self,x):
        if x is "?": return x
        self.n += 1
        self.some.sampleInc(x)
        d = x - self.mu
        self.mu += d/self.n
        self.m2 += d*(x-self.mu)
        self.hi = max(x,self.hi)
        self.lo = min(x,self.lo)
        if self.n >=2:
            self.sd = (self.m2/(self.n - 1 + 10**-32))**0.5
        return x

    def numDec(self,x):
        if x is "?": return x
        if self.n == 1: return x
        self.n -= 1
        d = x - self.mu
        self.mu -= d/self.n
        self.m2 -= self.m2 - d*(x - self.mu)
        if self.n >= 2:
            self.sd = (self.m2/(self.n - 1 + 10**-32))**0.5
        return x

    """Normalization"""
    def numNorm(self,x):
        return x=="?" and 0.5 or (x-self.lo) / (self.hi-self.lo + 10**-32)

    def numXpect(i,j):
        n = i.n + j.n +0.0001
        return i.n/n * i.sd+ j.n/n * j.sd
        
"""test
@O.k
def testNum():
    n = Num([4,10,15,38,54,57,62,83,100,100,174,190,215,225,233,250,260,270,299,300,306,333,350,375,443,475,525,583,780,1000])
    assert abs(n.mu - 270.3) < 0.1
    assert abs(n.sd - 231.946) < 0.1
    print(n.mu, n.sd)
"""
