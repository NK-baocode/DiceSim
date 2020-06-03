import numpy as np

n = 1
dnum = 0
dvalue = 0
dtotal = 0

dnumin = input('How many dice would you like to roll?\n')
dsides = input('How many sides per die?\n')

dnumin = int(dnumin)
dsides = int(dsides)

for i in range(dnumin):
  d = np.arange(1, (dsides+1), 1)
  dvalue = (np.random.choice(d))
  print(f'Die #{n} rolled {dvalue}')
  dtotal = dvalue + dtotal
  n = n + 1

print(f'You rolled {dtotal} in total')



