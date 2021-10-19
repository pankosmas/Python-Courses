# This program examines how lucky is finally a game that generates
# "random" dices in 1 million times.

#from datetime import datetime
from random import randrange
#from random import seed

#seed(datetime.now())

numbers = {}
N = 1000000

for i in range(1, 7):
    numbers[i] = 0

for _ in range(N):
    num = randrange(1, 7)
    numbers[num] += 1

for i in range(1, 7):
    print(str(i) + ": " + str(numbers[i]/N))

