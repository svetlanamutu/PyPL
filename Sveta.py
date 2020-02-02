def fibo2(n) :
  i = 1
  j = 1
  k=0
  while(k<n) :
    ij=i+j
    i=j
    j=ij
    k+=1
  return i

def subset(Xs) :
  if not Xs : yield Xs # ir empty
  else :
    X = Xs[0] # head
    Ys = Xs[1:] # tail
    for Zs in subset(Ys) :
      yield Zs # inherit from the subsets of tail
      yield [X] + Zs # extend the subsets of tail


def t3():
   for t in subset([0, 1, 2, 3]): print(t)


def abc(n) :
  for i in range(2**n) :
    l=list(str(bin(i))[2:].zfill(n))
    yield deff(l)

def deff(Xs) :
  k=0
  for j in Xs:
    if j == '1':
      yield k
    k=k+1


def t3() :
  for t in abc(5) : print(set(t))


def t4() :
  for t in abc(5) :
    if t==set():
      yield {}
    yield set(t)


