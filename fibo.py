import time
l = [0, 1]
i = 2
while True:
  l.append(l[i-1] + l[i-2])
  print(l[i-1] + l[i-2])
  time.sleep(0.25)
  i+=1
