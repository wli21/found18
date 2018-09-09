"""
Rewrite from sample.luo
list index in luo start from 1

@author: Weijia Li
"""

from __future__ import division
from testEngine import O
import random, math

class Sample:

    def __init__(self,max_sample = 128):
        self.max_sample = max_sample
        self.n = 0
        self.sorted = False
        self.some = []

    def sampleInc(self,x):
        self.n += 1
        now = len(self.some)
        if now < self.max_sample:
            self.sorted = False
            self.some.append(x)
        elif random.random() < now/self.n:
            self.sorted = False
            self.some[math.floor(random.random()*now)] = x
        return x

    def sampleSorted(self):
        if not self.sorted:
            self.sorted = True
            self.some.sort()
        return self.some

    def nth(self,n):
        s = self.sampleSorted()
        return s[min(len(s),max(0,math.floor(len(s)*n)))]


"""test"""
@O.k
def testSample():
    random.seed(1)
    s = [ Sample(2**i) for i in range(5,11)]
    for i in range(10000):
        y = random.random()
        for j,t in enumerate(s):
            t.sampleInc(y)

    for _,t in enumerate(s):
        print(t.max_sample, t.nth( 0.5))
        assert abs(t.nth(0.5)-0.5) < 0.2
