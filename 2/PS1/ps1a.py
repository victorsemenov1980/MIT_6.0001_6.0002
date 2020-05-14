###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows={}
    with open(filename,'r') as file:
        for row in file:
            text=row.split(sep=',')
            cows.update({text[0]:int(text[1].strip('\n'))})
    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_sorted={k: v for k, v in sorted(cows.items(), key=lambda item: item[1], reverse=True)}
    trips2=[]
    total_weight=0
    for i in range(len(cows_sorted)):
        trips=[]
        total_weight=0
        for k,v in cows_sorted.items():
            if total_weight+cows_sorted[k]<=limit:
                trips.append(k)
                total_weight+=cows_sorted[k]
                cows_sorted[k]=limit+10
        if trips!=[]:
            trips2.append(trips)
    return trips2

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips2=[]
    for partition in get_partitions(cows): 
        trips=[]
        total_weight=0
        for i in partition:
            for k in i:
                if k in cows:
                    total_weight+=cows[k]
                
            if total_weight<=limit:
                trips.append(i)
            total_weight=0
        if len(trips)!=len(partition):
            trips=[]
        if trips!=[]:
            trips2.append(trips)

    trips2.sort(key=len)
    return trips2[0]
        
# Problem 4
def compare_cow_transport_algorithms(code):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time() 
    print('Testing',code)
    code
    end = time.time() 
    print (end,start)
    print(len(code))





































