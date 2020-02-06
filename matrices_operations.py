# Program to add two matrices using nested loop



def add(x,y):
  result = [[x[i][j] + y[i][j]  for j in range
  (len(x[0]))] for i in range(len(x))] 
  return result


def multiply(x,y):
  r=[]
  m=[]
  for i in range(len(x)):
      for j in range(len(y[0])):
          sums=0
          for k in range(len(y)):
              sums=sums+(x[i][k]*y[k][j])
          r.append(sums)
      m.append(r)
      r=[]
  return m


def transpose(x):
  result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
  return result