import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
letters='aeioubcdfghjklmnpqrstvwxyz'
HAND_SIZE = 25

SCRABBLE_LETTER_VALUES = {
    'a': 1,'*':0, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "words.txt"


def load_words():
   
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
# Problem #1: Scoring a word

def get_word_score(word, n):
   
    actual_value=0
    word=word.lower()
    for char in word:
        if char in SCRABBLE_LETTER_VALUES:
            actual_value+=SCRABBLE_LETTER_VALUES[char]
        else:
            actual_value += 0
    
    if (7*len(word)-3*(n-len(word)))>1:
        word_length=7*len(word)-3*(n-len(word))
    else:
        word_length=1
    
    score=actual_value*word_length
    return score

def display_hand(hand):
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line


def deal_hand(n):
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    hand.update( {'*' : 1} )
    
    return hand


# Problem #2: Update a hand by removing letters

def update_hand(hand, word):
   
    new_hand=hand.copy()
    word=word.lower()
    for letter in word:
        if (hand[letter]-1)>0:
            new_hand[letter]-=1
        else:
            del new_hand[letter]
        
            
    return new_hand

    
# Problem #3: Test word validity

def is_valid_word(word, hand, word_list):
    
    check_hand=hand.copy()
    word=word.lower()
    boolean=[]
    x=boolean.count(0)
    if word in word_list:
        for letter in word:
            if letter in hand:
                check_hand[letter]-=1
                if check_hand[letter]<0:
                    boolean+=[0]
                else:
                    boolean+=[1]        
            else:
                x=10
                break
            
               
    else:
        x=10
        return False
        # print('Your word does not exist')
   
    if x>=1:
        return False
        # print('You used letter that is not in your hand')
            
    else:
        return True
        # print('Your word is accepted')
  


# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    
    hand_length=[]
    for key in hand:
        hand_length.append(hand[key])
   
    length=sum(hand_length)
    return length
   

def play_hand(hand, word_list):
    n=HAND_SIZE
    while n >0:
         print('')
         word=str(input('Please enter your word, if you want to stop - enter !!. '))
         word=word.lower()
         print('')
         new_hand=update_hand(hand, word)
         score=get_word_score(word, n)
         total_score=[]
        
         if word=='!!':
            print('End game')
            break
         else:       
            if is_valid_word(word, hand, word_list)==True:
                total_score.append(score)
                print('Your total score is') 
                print(sum(total_score))
                print('')
                print('You updated hand is:')
                hand=new_hand
                display_hand(hand)
                length=calculate_handlen(hand)
                n=length
                
            else:
                print('You word is rejected')
    
    
# Problem #6: Playing a game

#

def substitute_hand(hand, letter):
   new_letter=random.choice(letters)
   subs_hand=hand.copy()
   x=hand[letter]
   subs_hand[new_letter]=x
   del subs_hand[letter]
   return subs_hand
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    

n=HAND_SIZE
word_list = load_words()
hand=deal_hand(n)
print('')
print('Your first hand is:')
display_hand(hand)
play_hand(hand, word_list)
    
