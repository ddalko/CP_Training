# UVA 11581 - Gird Successors
# 2019.09.19
# Prog AdcKi
# AC

import sys

def f(g):
  sizeIterable = range(3)
  temp = [[0] * 3 for i in sizeIterable]

  temp[0][0] = (g[0][1] + g[1][0]) % 2
  temp[0][1] = (g[0][0] + g[1][1] + g[0][2]) % 2
  temp[0][2] = (g[0][1] + g[1][2]) % 2

  temp[1][0] = (g[0][0] + g[1][1] + g[2][0]) % 2
  temp[1][1] = (g[0][1] + g[1][0] + g[1][2] + g[2][1]) % 2
  temp[1][2] = (g[0][2] + g[1][1] + g[2][2]) % 2

  temp[2][0] = (g[1][0] + g[2][1]) % 2
  temp[2][1] = (g[2][0] + g[1][1] + g[2][2]) % 2
  temp[2][2] = (g[2][1] + g[1][2]) % 2
  return temp

def isAllZero(g):
  for i in range(3):
    for j in range(3):
      if g[i][j] == 1:
        return False
  return True

test_case = int(sys.stdin.readline())
for tc in range(test_case):
  g = []
  n = 3
  while n > 0: 
    str = sys.stdin.readline().strip()
    if len(str) == 0: continue
    g.append(list(map(int, str)))
    n -= 1
  cnt = -1
  while isAllZero(g) == False:
    g = f(g)
    cnt += 1
  print(cnt)