from __future__ import division
from collections import defaultdict
from collections import Counter
from functools import partial,reduce
import re,traceback
import math,random


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

@O.k
def page5():
  two_plus_three = 2 + \
                   3
  assert two_plus_three==5

@O.k
def page6():
  result = math.sqrt(9)
  assert result==3

@O.k
def page7():
  result = 5 / 2
  assert result==2.5

@O.k
def page8():
  def apply_to_one(f):
    return f(1)

  result = apply_to_one(lambda x: x * 2)
  assert result==2

@O.k
def page9():
  not_tab_string = r"\t"
  assert len(not_tab_string)==2

@O.k
def page10():
  a = 1
  try:
    0 / 0
  except ZeroDivisionError:
    a = 2
  assert a==2

@O.k
def page11():
  x = range(10)
  assert x[4]==4

@O.k
def page12():
  _, y = [1, 2]
  assert y==2

@O.k
def page13():
  x, y = 1, 2
  x, y = y, x
  assert x==2

@O.k
def page14():
  grades = { "Joel" : 80, "Tim" : 95 }
  grades["Kate"] = 100
  assert len(grades)==3

@O.k
def page15():
  dd_list = defaultdict(list)
  dd_list[2].append(1)
  assert dd_list[2][0]==1

@O.k
def page16():
  c = Counter([0, 1, 2, 0])
  number,_ = c.most_common(10)[0]
  assert number==0

@O.k
def page17():
  item_list = [1, 2, 3, 1, 2, 3]
  item_set = set(item_list)
  assert len(item_set)==3

@O.k
def page18():
  a = 0
  for x in range(5):
    a+=x
  assert a==10

@O.k
def page19():
  one_is_less_than_two = 1 < 2
  assert one_is_less_than_two is True

@O.k
def page20():
  assert all([])==True

@O.k
def page22():
  x = sorted([-4,1,-2,3], key=abs, reverse=True)
  assert x[0]==-4

@O.k
def page23():
  pairs = [(x, y)
           for x in range(10)
           for y in range(x + 1, 10)]
  x,y = pairs[0]
  assert y==1

@O.k
def page24():
  i = 0
  while i < 10:
    yield i
    i += 1
  assert i==10

@O.k
def page25():
  random.seed(10)
  r = random.random()
  random.seed(10)
  assert r==random.random() 

@O.k
def page26():
  assert not re.match("a", "cat") is True

@O.k
def page27():

  class Person:
    def __init__(self, name="", age=0):
      self.name = name
      self.age = age

    def grow(self):
      self.age+=1

    def getAge(self):
      return self.age
  
  p = Person("Bob",20)
  p.grow()
  assert p.getAge()==21

@O.k
def page28():
  def double(x):
    return 2 * x

  xs = [1, 2, 3, 4]
  twice_xs = list(map(double, xs))
  assert twice_xs[0]==2

@O.k
def page29():
  def multiply(x, y):
    return x * y
  
  xs = [1, 2, 3, 4]
  x_product = reduce(multiply, xs)
  assert x_product==24

@O.k
def page30():
  n = range(5)
  a = 0
  for i, j in enumerate(n):
    a += i + j
  assert a==20

@O.k
def page31():
  pairs = [('a', 1), ('b', 2), ('c', 3)]
  _, numbers = zip(*pairs)
  assert numbers[0]==1

@O.k
def page32():
  def other_way_magic(x, y, z):
    return x + y + z
  x_y_list = [1, 2]
  z_dict = { "z" : 3 }
  assert other_way_magic(*x_y_list, **z_dict)==6  

@O.k
def page33():
  def doubler(f):
    def g(*args, **kwargs):
      return 2 * f(*args, **kwargs)
    return g
  
  def f2(x, y):
    return x + y
  g = doubler(f2)
  assert g(1, 2)==6



if __name__== "__main__":
  O.report()
