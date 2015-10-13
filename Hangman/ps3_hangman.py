# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "D:/Work/Hangman_doc/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    i = ''
    for i in secretWord:
        if (i in lettersGuessed):
            return True
        else:
            return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessWord = ''
    i = ''
    for i in secretWord:
        if i in lettersGuessed:
            guessWord += i
        else:
            guessWord += '_'
    return guessWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    restLetters = ''
    i = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            restLetters += i
    return restLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    #secretWord = chooseWord(wordlist)
    count = 0
    lettersGuessed = []
    theGuessedWord = ''
    theRest = []
    guess = ''
    
    print 'The secret word contains ' + str(len(secretWord)) + ' letters'
    print 'You have 8 chances to guess the word'
    
    for count in range(8):
        print 'Your #' + str(count) + ' guess: '
        ''' Need a input checking function here:
            Check if input is a letter or not
            Check if input letter has already picked or not
        '''
        lettersGuessed.append(guess)
        theGuessedWord = getGuessedWord(secretWord,lettersGuessed)
        theRest = getAvailableLetters(lettersGuessed)
        if guess.lower() in secretWord:
            print 'Nice job!'
        elif (isWordGuessed(secretWord, lettersGuessed) == True):
            print 'You''ve completed the job' 
            print 'The answer is ' + secretWord
            break
        else: print 'Wrong! Try another letter!'
        print 'Current status of the game:\n'
        print 'You have discovered: ' + theGuessedWord
        print 'The letters have not been picked yet: ' + theRest
        
    if (isWordGuessed(secretWord, lettersGuessed) == False):
        print '\nGame over! The secret word is ' + secretWord

    return 0




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
