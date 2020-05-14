# def get_permutations_count(n):
#     if n==1:
#         return 1 
#     else:
#         return n*get_permutations_count(n-1)

# permutation_string='abcd'
# print('Current permutation string is: ',permutation_string)
# letters=list(permutation_string)  
# print('Converting string to a list for permutations: ',letters)
# n=len(permutation_string) 
# print('Number of permutations will be: ',get_permutations_count(n))

# # Python function to print permutations of a given list 
# def permutation(lst): 
  
#     # If lst is empty then there are no permutations 
#     if len(lst) == 0: 
#         return [] 
  
#     # If there is only one element in lst then, only 
#     # one permuatation is possible 
#     if len(lst) == 1: 
#         return [lst] 
  
#     # Find the permutations for lst if there are 
#     # more than 1 characters 
  
#     l = [] # empty list that will store current permutation 
  
#     # Iterate the input(lst) and calculate the permutation 
#     for i in range(len(lst)): 
#         m = lst[i] 
#         print('M=',m)
  
#         # Extract lst[i] or m from the list.  remLst is 
#         # remaining list 
#         remLst = lst[:i] + lst[i+1:] 
#         print('Remainin list=',remLst)
  
#         # Generating all permutations where m is first 
#         # element 
#         for p in permutation(remLst): 
#             print('P is=',p)
#             l.append([m] + p) 
#             print('Final list=',l)
#     return l 
  
  
# # Driver program to test above function 

# for p in permutation(letters): 
#     print(p )
  
# import itertools
# print(list(itertools.permutations(letters)))

# def permutate(seq):
#     """permutate a sequence and return a list of the permutations"""
#     if not seq:
#         return [seq]  # is an empty sequence
#     else:
#         temp = []
#         for k in range(len(seq)):
#             part = seq[:k] + seq[k+1:]
#             print (k, part)  # test
#             for m in permutate(part):
#                 temp.append(seq[k:k+1] + m)
#                 print (m, seq[k:k+1], temp)  # test
#         return temp

# for temp in permutate(letters):
#     print(temp)
#



#
# Trying to permutate iteratevily
# if len(letters)<=1:
#     print('There is empty string or single character string')
# base=[]
# base2=[]
# fin=[]
# for i in range(len(letters)):
#     base.append(letters[i])
#     # print(base)
#     m=base[i]
#     # print(m)
#     base2=letters[:i]+letters[i+1:]
#     # print(base2)
#     if len(base2)>2:
        
# def get_permutations_count(n):
#     if n==1:
#         return 1 
#     else:
#         return n*get_permutations_count(n-1)


# def permutation(lst): 
  
    
#     if len(lst) == 0: 
#         return [] 
  
#     if len(lst) == 1: 
#         return [lst] 
  
#     l = [] 

#     for i in range(len(lst)): 
#        m = lst[i] 
#        print('M=',m)

#        remLst = lst[:i] + lst[i+1:] 
#        print('Remainin list=',remLst)

#        for p in permutation(remLst): 
#            # print('test')
#            print('P is=',p)
#            l.append([m] + p) 
#            print('Final list=',l)
#     return l 
  
permutation_string='abcd'
print('Current permutation string is: ',permutation_string)
letters=list(permutation_string)  
print('Converting string to a list for permutations: ',letters)
n=len(permutation_string) 
# print('Number of permutations will be: ',get_permutations_count(n))

# for p in permutation(letters): 
#     print(p )

def permute(s):
  out = []
  if len(s) == 1:
    return s
  else:
    for i,let in enumerate(s):
        print('test1')
        for perm in permute(s[:i] + s[i+1:]):
            print('test2')
            out += [let + perm]
  return out

l = permute(letters)
print(l)



