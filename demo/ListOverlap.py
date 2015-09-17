'''
Created on Sep 15, 2015
Exercise for 2 lists interaction.
http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
@author: TungPT10
'''
import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []

a = random.sample(range(100), 10)
b = random.sample(range(10), 10)
c = []

print a
print b
for i in a:
    if (i in b) and (i not in c):
        c.append(i)
print c