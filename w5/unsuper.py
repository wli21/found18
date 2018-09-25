from __future__ import division
from collections import defaultdict
from lib.testEngine import O
from lib.rows import rows
from lib.num import Num
import random, math, re, sys, operator

unsuper_enough,unsuper_margin = 0.5,1.05

def dump(a,sep = "\t"):
	for i in a:
		print(sep.join(str(e) for e in i))

def ksort(k,t):
	t = sorted(t, key=lambda x: str(x[k]))
	return t 

def unsuper(data):
	rows = data.rows
	enough = len(rows)**unsuper_enough

	def band(c,lo,hi):
		if lo == 0:
			return ".." + str(rows[hi][c])
		elif hi == most:
			return str(rows[lo][c]) + ".."
		else:
		  return str(rows[lo][c]) + ".." + str(rows[hi][c])

	def argmin(c,lo,hi):
		cut  = None
		if (hi - lo > 2*enough):
			l,r = Num(), Num()
			for i in range(lo,hi+1): r.numInc(rows[i][c])
			best = r.sd
			for i in range(lo,hi+1):
				x = rows[i][c]
				l.numInc(x)
				r.numDec(x)
				if l.n >= enough and r.n >= enough:
					tmp = Num.numXpect(l,r) * unsuper_margin
					if tmp < best:
						cut,best = i, tmp
		return cut

	'''hi is index of the last row'''
	def cuts(c,lo,hi,pre):
		txt = pre + str(rows[lo][c]) + ".. " + str(rows[hi][c])
		cut = argmin(c,lo,hi)
		if cut:
			print(txt)
			cuts(c,lo,   cut, pre + "|.. ")
			cuts(c,cut+1, hi, pre + "|.. ")
		else:
			b = band(c,lo,hi)
			print(txt + " (" + b + ")")
			for r in range(lo,hi+1):
				rows[r][c]=b

	'''Our data sorts such that all the "?" unknown values
	-- are pushed to the end. This function tells us
	-- where to stop so we don't run into those values.
	'''
	def stop(c,t):
		for i in range(len(t)-1,-1,-1): 
			if t[i][c] != "?" : return i
		return 0

	'''For all numeric indpendent columns, sort it and 
	-- try to cut it. Then `dump` the results to standard output.
	'''
	#print(str(len(rows)) + " rows in total")
	for c  in data.indeps:
		if c in data.nums:
			rows = ksort(c,rows)
			most = stop(c,rows)
			#dump(rows)
			print("\n-- " + data.name[c] + ": " + str(most) + "----------\n")
			cuts(c,0,most,"|.. ")
	print(", ".join(data.name).replace("$","")) 
	dump(rows)

def mainUnsuper(s):
	unsuper(rows(s))

@O.k
def testUnsuper():
	print("\nweatherLong.csv\n")
	mainUnsuper("data/weatherLong.csv")