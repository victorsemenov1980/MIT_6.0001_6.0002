
import math
import random
import string
WORDLIST_FILENAME = "words.txt"
hand={'a':1,'h':1,'o':2,'n':1,'*':1,'e':1,}
word='hone*'
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
letters='aeioubcdfghjklmnpqrstvwxyz'
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

# def update_hand(hand, word):
   
#     new_hand=hand.copy()
#     word=word.lower()
#     for letter in word:
#         if (hand[letter]-1)>0:
#             new_hand[letter]-=1
#         else:
#             del new_hand[letter]
        
            
#     return new_hand

def is_valid_word(word, hand, word_list):
    
    check_hand=hand.copy()
    word=word.lower()
    boolean=[]
    x=boolean.count(0)
    if '*' in word:
        s=list(word)
        print(s)
        for char in VOWELS:
            for i in s:
                if s[i]=='*':
                    s[i]=char
                    word.join(s)
            if word in word_list:
                print('hooray')
                break
            else:
                print('word does not exist')
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
        print('Your word does not exist')
        x=10
    
    if x>=1:
        print('You used letter that is not in your hand')
            
    else:
        print('Your word is accepted')
word_list = load_words()
is_valid_word(word, hand, word_list)
              

    

# def calculate_handlen(hand):
    
#     hand_length=[]
#     for key in hand:
#         hand_length.append(hand[key])
   
#     length=sum(hand_length)
#     return length


# calculate_handlen(hand)

# def substitute_hand(hand, letter):
#    new_letter=random.choice(letters)
#    subs_hand=hand.copy()
#    x=hand[letter]
#    subs_hand[new_letter]=x
#    del subs_hand[letter]
#    return subs_hand
   
   
#    print(subs_hand)
    
    
    
# print(hand)
# letter=str(input('Input the letter you want to change '))
# substitute_hand(hand, letter)

  