# binary and binary-unary (Mozkin) tree generators

import graphvizTree as gt
import time

# binary tree of size n
# size = number of in ternal nodes
def bin(n) :
  if n==0 : 
    yield ()
  else :
    for k in range(0,n) :    
      for l in bin(k) :
        for r in bin(n-1-k) :        
          yield (l,r)

# binary-unary (Motzkin) tree of size n
def mot (n) :
  if n==0 : 
    yield ()
  else :
    for m in mot(n-1) :
      yield [m]
    for k in range(0,n-1) :    
      for l in mot(k) :
        for r in mot(n-2-k) :        
          yield (l,r)

# rose tree (multi-way tree) of size n
def rose(n):
  if n == 0:
    yield []
  else:
    for k in range(0, n):
      for l in rose(k):
        for r in rose(n - 1 - k):
          yield [l] + r

# counts trees of size n generated by f
def countFor(f,n) :
  for i in range(n) :
    count = 0
    for t in f(i) : 
      count+=1
    yield count

# returns a list of counts for trees up to size n, generated by f
def countsFor(mes,f,n) :
  print(mes)
  print([c for c in countFor(f,n)])
  print("")

# prints representations that can be read back for
# all trees of size n generated by f
def showFor(mes,f,n) :
  print(mes)
  for t in f(n) :
    print(t)
  print("")

# depicts, using graphviz, one by one,
# all trees of size n generated by f
def picsFor(mes,f,n) :
  print(mes)
  for t in f(n) :
    print(t)
    gt.showSimple(t)
    time.sleep(3)
  print("")

# tests

def go() :
  showFor('Binary trees',bin,3)
  showFor('Motzkin trees',mot,4)
  showFor('Rose trees', rose, 3)

  countsFor('Binary trees',bin,12)
  countsFor('Motzkin trees',mot,12)
  countsFor('Rose trees', rose, 12)

  picsFor('Binary trees',bin,3)
  picsFor('Motzkin trees',mot,4)
  picsFor('Rose trees', rose, 4)

  print("done")

def test() :
  for n in range(6) :
    print(n,list(rose(n)))
