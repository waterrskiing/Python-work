'''
Created on Sep 16, 2015

@author: TungPT10
'''
# Filter even elements from a given list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if ((x % 2) == 0)]
print b