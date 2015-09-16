'''
Created on Sep 14, 2015

@author: TungPT10
'''
# from __builtin__ import str
import random

age = 0
times = 0
thisYear = 0

thisYear = random.randrange(0, 2100)
print "Hello, this is year: " + str(thisYear)
print "Give me your age!"
age = int(raw_input())
print "How many times you want this message to print out?"
times = int(raw_input())

while (times > 0):
    print "You will turn 100 years old on " + str(thisYear + 100 - age) + '\n'
    times -= 1