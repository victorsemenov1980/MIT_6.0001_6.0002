# def build_shift_dict(self, shift):
#     shift_dict={}
#     alphabeth=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     if 26<shift<1:
#         print('Your shift is out of legal range. Try again with shift from 1 to 25 inclusive')
#     else:
#         for i in range(len(alphabeth)):
#             print(i)

# s={}
# s.update({'A':'C'})
# s.update({'B':'C'})
# print(s)
# self_text='Victor Semenov!'
# shift=25
# shift_dict={}
# alphabeth_capitals=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# alphabeth_small=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# if shift>26 or shift<1:
#     print('Your shift is out of legal range. Try again with shift from 1 to 25 inclusive')
# else:
#     for i,j in enumerate(alphabeth_capitals):
#         shift_dict.update({alphabeth_capitals[i]:alphabeth_capitals[i+shift]})
#         if i==25:
#             break
#     for i,j in enumerate(alphabeth_small):
#         shift_dict.update({alphabeth_small[i]:alphabeth_small[i+shift]})
#         if i==25:
#             break
# x=shift_dict        
# print(x)
# #return shift_dict
# def apply_shift(self_text, shift):
#         '''
#         Applies the Caesar Cipher to self.message_text with the input shift.
#         Creates a new string that is self.message_text shifted down the
#         alphabet by some number of characters determined by the input shift        
        
#         shift (integer): the shift with which to encrypt the message.
#         0 <= shift < 26

#         Returns: the message text (string) in which every character is shifted
#               down the alphabet by the input shift
             
#         '''
#         encrypted=''
#         temp=[]
       
#         for char in self_text:
#             if char in shift_dict:
#                # print(shift_dict[char])
#                temp.append(shift_dict[char])
#                # print(temp)
#             else:
#                 # print(char)
#                 temp.append(char)
#                 # print(temp)
#         encrypted=''.join(temp)
#         print(encrypted)
            
            
# apply_shift(self_text, shift)   

# def load_words(file_name):
#     '''
#     file_name (string): the name of the file containing 
#     the list of words to load    
    
#     Returns: a list of valid words. Words are strings of lowercase letters.
    
#     Depending on the size of the word list, this function may
#     take a while to finish.
#     '''
#     print("Loading word list from file...")
#     # inFile: file
#     inFile = open(file_name, 'r')
#     # wordlist: list of strings
#     wordlist = []
#     for line in inFile:
#         wordlist.extend([word.lower() for word in line.split(' ')])
#     print("  ", len(wordlist), "words loaded.")
#     return wordlist

# def is_word(word_list, word):
#     '''
#     Determines if word is a valid word, ignoring
#     capitalization and punctuation

#     word_list (list): list of words in the dictionary.
#     word (string): a possible word.
    
#     Returns: True if word is in word_list, False otherwise

#     Example:
#     >>> is_word(word_list, 'bat') returns
#     True
#     >>> is_word(word_list, 'asdf') returns
#     False
#     '''
#     word = word.lower()
#     word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
#     return word in word_list

# word_list=load_words('words.txt')
# self_text='Uhbsnq Rdldmnu!'


# def decrypt_message(self_text):
        
#         final=[]
#         list_of_string=[]
#         decrypted=''
#         temp=[]
#         shift_dict={}
#         alphabeth_capitals=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#         alphabeth_small=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#         shift=0
#         while shift<=25:
            
#             for i,j in enumerate(alphabeth_capitals):
#                 shift_dict.update({alphabeth_capitals[i]:alphabeth_capitals[i+shift]})
#                 if i==25:
#                     break
#             for i,j in enumerate(alphabeth_small):
#                 shift_dict.update({alphabeth_small[i]:alphabeth_small[i+shift]})
#                 if i==25:
#                     break
#             for char in self_text:
#                 if char in shift_dict:
#                     temp.append(shift_dict[char])
#                 else:
#                     temp.append(char)
#             decrypted=''.join(temp)
#             final.append(temp)
#             shift+=1
#             temp=[]
#             list_of_string.append(decrypted)
#         wordfin=[]
#         for i,j in enumerate(list_of_string):
#             word=list_of_string[i].split()
#             for key,value in enumerate(word):
#                 if is_word(word_list, word[key])==True:                
#                     wordfin.append(word[key])
                    
#                     decrypted=''.join(wordfin)
               
#             wordfin=[]
#         print(decrypted)
        
       
                 
            
            
            
# decrypt_message(self_text)   


class Message(object):
    def __init__(self, text):
        self.message_text=text

    def get_message_text(self):
        # return self.message_text
        print(self.message_text)
        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self, text)
        self.shift=shift
    
    def get_shift(self):
        # return self.shift
        print(self.shift)
    def test_self(self):
        print('test')

text=str(input('enter text :'))
shift=int(input('enter shift: '))
c=PlaintextMessage(text, shift)
c.get_shift()
c.get_message_text()


























