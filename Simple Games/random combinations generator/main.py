# This program generates randomly 10 columns , each consists of
# 2 number 10-19 , 2 numbers 20-39 , an even 1-9 and one 40-49.
# Finally, it prints the output of all 10 randomly generated and
# different columns.
# while loops, randrange, datetime, sets, lists, control flow.

#from random import seed
from random import randrange
#from datetime import datetime

#seed(datetime.now())
counter = 0
columns = []

while True:
    column = set()

    #generate 2 numbers between 10-19
    rand_number = randrange(10, 20)
    column.add(rand_number)
    while True:
        rand_number = randrange(10, 20)
        if rand_number not in column:
            column.add(rand_number)
            break
    #generate 2 numbers between 20-39
    rand_number = randrange(20, 40)
    column.add(rand_number)
    while True:
        rand_number = randrange(20, 40)
        if rand_number not in column:
            column.add(rand_number)
            break
    #generate an even between 1-9
    rand_number = 2 * randrange(1,5)
    column.add(rand_number)
    #generate a number between 40-49
    rand_number = randrange(40, 50)
    column.add(rand_number)

    if column not in columns:
        columns.append(column)
        counter += 1
        if counter == 10:
            break

for column in columns:
    print(column)
