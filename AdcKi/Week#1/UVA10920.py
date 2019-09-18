# UVA 10920 - Spiral Tap
# 2019.09.18
# Prog by AdcKi
# AC

import sys
import math

while True:
  try: (n, k) = map(int, sys.stdin.readline().split())
  except IOError: break
  if n == 0 and k == 0: break
  factor = int(math.floor((math.sqrt(k) - 1.0) / 2.0))
  y = x = math.ceil(n / 2.0) + factor
  k -= int(math.pow(2 * factor + 1, 2))
  if k == 0:
    pass
  elif k <= 2 * (factor  + 1):
    y += 1
    x -= (k - 1)
  elif k <= 4 * (factor  + 1):
    k -= 2 * (factor + 1)
    x -= (2 * (factor + 1 ) - 1)
    y -= (k - 1)
  elif k <= 6 * (factor  + 1):
    k -= 4 * (factor + 1)
    y -= (2 * (factor + 1 ) - 1)
    x -= (2 * (factor + 1 ) - 1)
    x += k
  elif k <= 8 * (factor  + 1):
    k -= 6 * (factor + 1)
    y -= (2 * (factor + 1 ) - 1)
    x += 1
    y += k
  print('Line = %d, column = %d.' % (y, x))
  