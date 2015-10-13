'''
Created on Oct 12, 2015
Help function getGuessedWord
    - secretWord = string
    - letterGuessed = list
@author: TungPT10
'''

def getGuessedWord(secretWord, lettersGuessed):
    guessWord = ''
    i = ''
    for i in secretWord:
        if i in lettersGuessed:
            guessWord += i
        else:
            guessWord += '_'
    return guessWord

secretWord1 = 'thomas'
lettersGuessed1 = ['k', 'g', 'a', 'h', 'm', 'i', 's']
print getGuessedWord(secretWord1, lettersGuessed1)