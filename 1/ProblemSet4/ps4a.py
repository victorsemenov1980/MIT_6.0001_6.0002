# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations_count(n):
    if n==1:
        return 1 
    else:
        return n*get_permutations_count(n-1)


def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
       print('M=',m)
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
       print('Remainin list=',remLst)
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           print('P is=',p)
           l.append([m] + p) 
           print('Final list=',l)
    return l 
  
  
# Driver program to test above function 




if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here
permutation_string='abcd'
print('Current permutation string is: ',permutation_string)
letters=list(permutation_string)  
print('Converting string to a list for permutations: ',letters)
n=len(permutation_string) 
print('Number of permutations will be: ',get_permutations_count(n))

for p in permutation(letters): 
    print(p )