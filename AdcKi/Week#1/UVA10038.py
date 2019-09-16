# UVA 10038;BOJ 4383 - Jolly Jumpers
# 2019.09.15
# Prog by AdcKi
# AC

def isJolly(data):
  n = data[0]
  arr = data[1:]
  used = [0] * n
  used[0] = 1
  for i in range(1, n):
    dif = abs(arr[i] - arr[i - 1])
    if not 0 < dif < n:
      return False
    if used[dif] == 1:
      return False
    used[dif] = 1    
  for i in range(0, n):
    if used[i] == 0:
      return False
  return True

while True:
  try: line = input()
  except: break
  arr = list(map(int, line.split()))
  print(arr)
  if isJolly(arr):
    print('Jolly')
  else:
    print('Not jolly');