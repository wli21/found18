from __future__ import division
from collections import defaultdict
from testEngine import O
from num import Num
from sym import Sym
import random, math, re, sys

class Data:

    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self._class = None
        self.rows = []
        self.name = []
        self._use = []
        self.indeps = []

    '''def indep(self,c): return not self.w[c] and self.calss != c'''
    def indep(self,c): return not c in self.w and self.calss != c

    def dep(self,c): return not indep

    def header(self,cells):
        for c0,x in enumerate(cells):
            if not "?" in x:
                c = len(self._use)
                self._use.append(c0)
                self.name.append(x)
                if re.search("[<>$]", x):
                    self.nums[c] = Num()
                else: self.syms[c] = Sym()
                if re.search("<", x): self.w[c]  = -1
                elif re.search(">", x): self.w[c]  =  1
                elif re.search("!", x): self._class =  c
                else: self.indeps.append(c)
        return self
        
    def row(self,cells):
        l = len(self.rows)
        self.rows.append([])
        for c,c0 in enumerate(self._use):
            x = cells[c0]
            if x is not "?":
                if c in self.nums:
                    try: x = int(x)
                    except ValueError:
                        x= float(x)
                    self.nums[c].numInc(x)
                else:
                    self.syms[c].symInc(x)
            self.rows[l].append(x)
        return self
"""-------------end of calss data----------------"""

"""taken from data.py"""
def lines(s=None):
   "Return contents, one line at a time."
   if not s:
     for line in sys.stdin:
       yield line
   elif s[-3:] in ["csv","dat"]:
     with open(s) as fs:
       for line in fs: 
         yield line
   else:
     for line in s.splitlines():
       yield line

def rows1(src):
    data = Data()
    first = True
    for line in src:
        line = re.sub(r'([ \n\r\t]|#.*)', "", line)
        cells = line.split(",")
        if len(cells) > 0 and cells[0] != "":
            if first: data.header(cells)
            else: data.row(cells)
            first = False
    print("\t\t\tn\tmode\tfrequency\n")
    for key,val in data.syms.items():
        print(f'{key}\t{data.name[key]}\t\t{val.n}\t{val.mode}\t{val.most}')
    print("\n\t\t\tn\tmu\tsd\n")
    for key,val in data.nums.items():
        print(f'{key}\t{data.name[key]}\t\t{val.n}\t{val.mu:.2f}\t{val.sd:.2f}')
    return data

def rows(s):
    return rows1(lines(s))

@O.k
def testRows():
    print("\nweather.csv\n")
    rows("weather.csv")
    print("\nweatherLong.csv\n")
    rows("weatherLong.csv")
    print("\nauto.csv\n")
    rows("auto.csv")
