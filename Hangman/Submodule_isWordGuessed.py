'''
Created on Oct 12, 2015
Check help function isWordGuessed

@author: TungPT10
'''

def isWordGuessed(secretWord, lettersGuessed):
    i = ''
    for i in secretWord:
        if (i in lettersGuessed):
            return True
        else:
            return False

secretWord = 'abc'
lettersGuessed = 'mbcd'
print isWordGuessed(secretWord, lettersGuessed)