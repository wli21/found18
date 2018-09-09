"""
Rewrite from sym.luo

@author: Weijia Li
"""
from __future__ import division
from collections import defaultdict
from testEngine import O
import random, math

class Sym:

    def same(x): return x
    
    def __init__(self,inits=[],f=same):
        self.counts = defaultdict(int)
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None
        [self.symInc(x) for x in inits]

    def symInc(self,x):
        if x is "?": return x
        self._ent = None
        self.n += 1
        self.counts[x] += 1
        if self.counts[x] > self.most:
            self.most = self.counts[x]
            self.mode = x
        return x


    def symDec(self,x):
        self._ent = None
        self.n -= 1
        self.counts[x] -= 1
        return x

    def symEnt(self):
        if self._ent is None:
            self._ent = 0
            for _,n in self.counts.items():
                p = n/self.n
                self._ent -= p * math.log(p,2)
        return self._ent

"""test"""
@O.k
def testSym():
    s = Sym(['y','y','y','y','y','y','y','y','y','n','n','n','n','n'])
    assert abs(s.symEnt() - 0.9403) < 0.01
    print(s.symEnt())
