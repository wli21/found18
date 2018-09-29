from __future__ import division
from collections import defaultdict
from lib.testEngine import O
from lib.rows import rows
from lib.num import Num
from lib.dom import doms
import random, math, re, sys

super_enough,super_margin = 0.5,1.05

def dump(a,sep = "  "):
	for i in a:
		if isinstance(i[len(i)-1],float):
			i[len(i)-1] = str("%.2f" % i[len(i)-1])
		print(sep.join(str("%10s" % e) for e in i))

def ksort(k,t):
	t = sorted(t, key=lambda x: str(x[k]))
	return t 

def split_value(e_sd):
	total = 0
	result = 0
	for _,(n,sd) in e_sd.items():
		total += n
	for _,(n,sd) in e_sd.items():
		result += n/(total + 10**-32)*sd
	return result

def super(data,goal = None,enough = None):
	e_sd = {}
	rows = data.rows
	if goal is None:
		goal = len(rows[0])-1
	if enough is None:
		enough = len(rows)**super_enough

	def band(c,lo,hi):
		if lo == 0:
			return ".." + str(rows[hi][c])
		elif hi == most:
			return str(rows[lo][c]) + ".."
		else:
		  return str(rows[lo][c]) + ".." + str(rows[hi][c])

	def argmin(c,lo,hi):
		cut = None
		xl,xr = Num(), Num()
		yl,yr = Num(), Num()
		for i in range(lo,hi+1):
			xr.numInc(rows[i][c]) 
			yr.numInc(rows[i][goal])
		bestx = xr.sd
		besty = yr.sd # dom score
		mu    = yr.mu
		n = yr.n
		if (hi - lo > 2*enough):
			for i in range(lo,hi+1):
				x = rows[i][c]
				y = rows[i][goal]
				xl.numInc(x)
				xr.numDec(x) 
				yl.numInc(y)
				yr.numDec(y) 
				if xl.n >= enough and xr.n >= enough:
					tmpx = Num.numXpect(xl,xr) * super_margin
					tmpy = Num.numXpect(yl,yr) * super_margin
					if tmpx < bestx and tmpy < besty:
						cut,bestx,besty = i, tmpx, tmpy
		return cut,mu,n,besty

	def cuts(c,lo,hi,pre):
		txt = pre + str(rows[lo][c]) + ".." + str(rows[hi][c])
		cut,mu,n,sd = argmin(c,lo,hi)
		if cut:
			print(txt)
			cuts(c,lo,   cut, pre + "|.. ")
			cuts(c,cut+1, hi, pre + "|.. ")
		else:
			s = band(c,lo,hi)
			# store the # and sd for data fitts in this range
			e_sd[c]={}
			e_sd[c][s] = (n,sd)
			print(txt + " = " + str(math.floor(100*mu)))
			for r in range(lo,hi+1):
				rows[r][c]=s

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

	print("  ".join(str("%10s" % e) for e in data.name).replace(",",""))
	dump(rows)

	'''For splitter'''
	splitter, min_sd = None, None
	for c  in data.indeps:
		if c in data.nums:
			curr_sd = split_value(e_sd[c])
			if min_sd is None or curr_sd < min_sd:
				min_sd = curr_sd
				splitter = data.name[c]
			print("Expected sd when split on * " + data.name[c] + " * is " + str("%0.2f" %curr_sd))
	print("Splitter is: " + splitter + "\n")

def mainSuper(s):
	super(doms(rows(s)))

@O.k
def testSuper1():
	print("\nweatherLong.csv\n")
	mainSuper("data/weatherLong.csv")

@O.k
def testSuper1():
	print("\nauto.csv\n")
	mainSuper("data/auto.csv")
