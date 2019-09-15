# UVA 11340
# Newspaper
# Prog by AdcKi

import sys

test_case = int(sys.stdin.readline())
for tc in range(test_case):
  k = int(sys.stdin.readline())
  costs = dict()
  for i in range(k):
    [a, b] = sys.stdin.readline().split()
    costs[a] = int(b)
  l = int(sys.stdin.readline())
  sum = 0
  for i in range(l):
    line = sys.stdin.readline()
    for char in line:
      if char in costs:
        sum += costs[char]
  print('%.2f$' % (sum / 100))
  