class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc()) 
    return f


DATA1 ="""
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""

def lines(s):
   return s.split('\n')

def rows(src):
  lines = []
  join = ""

  for s in src:
    s = join + s.split('#')[0].strip()
    if s is not "" and s[-1] is not ',':
      lines.append(s)
      join = ""
    else:
      join = s

  return lines


def cols(src):
  row1 = src[0].split(',')
  ignore = [0 for _ in row1]
  
  for index,c in enumerate(row1):
      if '?' in c or '>' in c:
        ignore[index] = 1

  result = []

  for s in src:
    new_row = []
    row = s.split(',')
    for i in range(len(row1)):
      if not ignore[i]: 
        new_row.append(row[i])

    result.append(new_row)
    
  return result


def prep(src):
  row1 = src[0]
  is_float = [0 for _ in row1]
  
  for index,c in enumerate(row1):
      if '$' in c:
        is_float[index] = 1

  for i,row in enumerate(src[1:]):
    for j,r in enumerate(row):
      if is_float[j]: 
        src[i+1][j] = float(r)
    
  return src

def ok0(s):
  for row in prep(cols(rows(lines(s)))):
    print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)
