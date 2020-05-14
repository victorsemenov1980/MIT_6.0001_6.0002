import random
import string
secret_word='apple'




WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    
       
    return wordlist

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    print(string.ascii_lowercase) 
    print(get_available_letters(letters_guessed)) 
    
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    print(is_word_guessed(secret_word, letters_guessed))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    print(get_guessed_word(secret_word, letters_guessed)) 
    


def hangman(secret_word):
    letters_guessed=''
    number_of_guesses=6
    count_guesses=len(secret_word)
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long')
    print('*'*len(secret_word))
    print('You have',number_of_guesses,'guesses left')
    print('Available letters are:',string.ascii_lowercase) 
    guess=input('Please make your guess ')
    while count_guesses>1:
        if guess in secret_word:
            print('Good guess:')
            letters_guessed+=guess
            for char in secret_word:
                if char in letters_guessed:
                    print(char)
                else:
                    print('-')
            
            count_guesses-=1
            
            guess=input('Please make your guess ')
           
        
                
        else:
            print('Oops! That letter is not in my word:')
            for char in secret_word:
                if char in letters_guessed:
                    print(char)
                else:
                    print('-')
            number_of_guesses-=1
            print('you have',number_of_guesses,'guesses left')
            guess=input('Please make your guess ')
            
            if number_of_guesses==1:
                print('Game over')
                break
                

wordlist = load_words()

hangman(secret_word)


