# UVA 10855 - Rotated squares
# 2019.09.17
# Prog by AdcKi
# TLE

import sys
import math

def rotateSquare(n, Square):
  for i in range(n):
    Square[i] = list(Square[i])
  for x in range(int(math.ceil(n / 2.0))):
    for y in range(int(math.floor(n / 2.0))):
      swap = Square[x][y]
      Square[x][y] = Square[n - 1 - y][x]
      Square[n - 1 - y][x] = Square[n - 1 - x][n - 1 - y]
      Square[n - 1 - x][n - 1 - y] = Square[y][n - 1 - x]
      Square[y][n - 1 - x] = swap

  for i in range(n):
    Square[i] = ''.join(Square[i])
  return Square

def countSSinBS(n, m, BS, SS):
  cnt = 0
  for i in range(n - m + 1):
    for j in range(n - m + 1):
      flag = False
      for k in range(m):
        for l in range(m):
          if BS[i + k][j + l] != SS[k][l]:
            flag = True
            break
        if flag == True:
          break
      if flag == False:
        cnt += 1
  return cnt

while True:
  try: (n, m) = map(int, sys.stdin.readline().split())
  except: break
  if n == 0 and m == 0: break
  BS = []
  SS = []
  for i in range(n):
    str = sys.stdin.readline()
    BS.append(str)
  for i in range(m):
    str = sys.stdin.readline()
    SS.append(str)
  for rotateCount in range(4):
    print(countSSinBS(n, m, BS, SS), end = ' ')
    SS = rotateSquare(m, SS)
  print()