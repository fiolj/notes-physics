#! /usr/bin/ipython
# -*- coding: utf-8 -*-
# import re
import numpy as np

# import matplotlib.pyplot as plt


# import scipy as sp
def find_eigenvector_text(fname):
  """ Identifica la parte del archivo de NWChem donde estan los autovectores
      y devuelve una lista con las líneas relevantes
  """
  with open(fname) as f:
    for l in f:
      if u'NORMAL MODE EIGENVECTORS IN CARTESIAN COORDINATES' in l:
        break
    useful = []
    for l in f:

      # L= re.sub(' +',' ',l.strip())
      L = ' '.join(l.split())
      # L= l
      if L.strip() != '':
        useful.append(L)
      if u'Normal Eigenvalue' in l:
        break
  return useful[2:-2]


def read_eigenvectors(filename, lim_freq=0.):
  """Lee el archivo que sale del NWChem y extrae la información de frecuencias y modos:
  input: filename donde están los datos
  lim_freq: frecuencia mínima para ser considerada vibración

  devuelve: freq, X
  --------

  donde:
    freq: Vector con las frecuencias en cm^{-1}
    X: Matriz donde X[j] es el desplazamiento normalizado del átomo j+1 para cada modo
  """

  s = find_eigenvector_text(fname)
  freq = []
  datos = []
  # i = 0
  for l in s:
    if u'Frequency' in l:
      freq.extend(map(float, l[10:].strip().split()))
      datos.pop()
      # i = 0
    else:
      datos.append(map(float, l.strip().split())[1:])
      # i += 1

  freq = np.array(freq)
  X = np.c_[datos[:21], datos[21:42], datos[42:63], datos[63:]]

  X = X.compress(freq > lim_freq, axis=1)
  freq = freq.compress(freq > lim_freq)
  for i, x in enumerate(X):
    X[i] = x / np.sqrt(np.dot(x, x))
  return freq, X


if __name__ == '__main__':
  fname = "../workbench/sf6.out11713"
  frec, X = read_eigenvectors(fname, lim_freq=30.)
  s = "v = {}".format(X)
  s += "w = {}".format(frec)
  fo = open('../workbench/sf6_vec.dat', 'w')
  fo.write(s)
  fo.close()
