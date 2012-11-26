# http://www.spotify.com/uk/jobs/tech/best-before/
# Paolo Boschini, 2012-11-26

import datetime
import sys
import itertools

input = raw_input()

best_before = None
for x in itertools.permutations(input.split('/')):
  try:
    current = datetime.date(int(x[0]) % 1000 + 2000, int(x[1]), int(x[2]))
    if best_before == None or best_before > current:
      best_before = current
  except ValueError:
    pass

if best_before != None:
  print best_before
else:
  print '%s is illegal' % input