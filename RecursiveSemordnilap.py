'''
Created on Sep 18, 2015

@author: TungPT10
'''
#Check if 2 strings are Semordnilap in recursive way.

def semordnilap(str1, str2):
    if not len(str1) and len(str2): return False
    if not len(str1) or not len(str2): return False
    if str1[0] != str2[-1]: return False
    else: return True
    return semordnilap(str1[:-1], str2[1:])

print str(semordnilap("boob", "boob"))