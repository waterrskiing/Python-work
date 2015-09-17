'''
Created on Sep 15, 2015
Exercise for lists in Python
http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
@author: TungPT10
'''

x = 0
a = []

print "Give me a number: "
x = int(raw_input('-->'))
for i in range(1, x + 1):
    if ((x % i) == 0):
        a.append(i)
print a