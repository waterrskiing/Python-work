def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string

    restLetters = ''
    i = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            restLetters += i
    return restLetters

lettersGuess1 = ['a', 'b', 'c']
print getAvailableLetters(lettersGuess1)
